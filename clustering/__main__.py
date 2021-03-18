# type: ignore[attr-defined]

import random
from enum import Enum
from typing import Optional
from pathlib import Path
import typer
import pandas as pd
import numpy as np

from clustering import __version__
from clustering.clustering import label_clusters


app = typer.Typer(
    name="clustering",
    help="CLI to apply Leiden clustering to an array of values",
    add_completion=False,
)


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(
            f"[yellow]clustering[/] version: [bold blue]{__version__}[/]"
        )
        raise typer.Exit()


@app.command(name="", context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
def main(
    input: str = typer.Argument(..., help="Name of the input data matrix, items in rows and observations in columns."),
    output: str = typer.Argument(..., help="Name to use for output file."),
    resolution: float = typer.Option(1.0, help="Resolution at which to cluster."),
    n_neighbors: int = typer.Option(30, help="Minimum number of neighbors required for a cluster"),
    version: bool = typer.Option(
        None,
        "-v", "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the clustering package.",
    ),
) -> None:
    input_df = Path(input)

    if not input_df.exists():
        raise FileNotFoundError
    else:
        df = pd.read_csv(input_df)
    
    output_array = label_clusters(data_df=df, resolution=resolution, n_neighbors=n_neighbors,)


    np.savetxt(fname=Path(output), X=output_array.astype(int), fmt="%d", delimiter=",",)

if __name__ == "main":
    typer.run(app)