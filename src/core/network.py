import pypsa
import os



def load_network(file_path: str) -> pypsa.Network:
    """
    Load a PyPSA network from a given file path.

    Parameters:
    - file_path: str: Path to the network file.

    Returns:
    - pypsa.Network: Loaded network.
    """

    # Ensure the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at {file_path}")

    # Determine file extension to load appropriate format
    _, ext = os.path.splitext(file_path)

    if ext not in ['.csv', '.nc']:  # Adjust supported extensions as needed
        raise ValueError(f"Unsupported file format: {ext}")

    # Load the network
    network = pypsa.Network(import_name=file_path)

    return network
