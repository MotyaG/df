import typer
import os

fs_list = [
    "ext4",
    "btrfs",
    "xfs",
    "vfat",
    "exfat",
    "reiserfs"
]

def make_fs(disk, selected_fs):
    print(f"Formatting {disk} to filesystem {selected_fs}")
    os.system(f"mkfs -t {selected_fs} {disk}")
    print("Formatted!")

def write_iso(disk, selected_file):
    print(f"Writing ISO {selected_file} to {disk}")
    os.system(f"dd if={selected_file} of={disk} bs=4M status=progress")
    print("Written!")

def main(type: str, disk: str, selected_fs: str = "", selected_file: str = ""):
    if type == "format":
        if selected_fs == "":
            typer.Exit("Select a filesystem.")
        else:
            make_fs(disk, selected_fs)
    elif type == "write":
        if selected_file == "":
            typer.Exit("Select an ISO file.")
        else:
            write_iso(disk, selected_file)

if __name__ == "__main__":
    typer.run(main)
