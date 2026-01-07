def list_files(parent_directory:dict, current_filepath:str=""):
    def get_file_paths(fpaths:list, root, curr_path):
        if root is None:
            fpaths.append(curr_path)

        if isinstance(root, dict):
            child_nodes = root.keys()
            for child_node in child_nodes:
                get_file_paths(fpaths, root[child_node], f"{curr_path}/{child_node}")
    file_paths = []
    get_file_paths(file_paths, parent_directory, current_filepath)
    return file_paths

test_input = {
    "Documents": {
        "Proposal.docx": None,
        "Report": {"AnnualReport.pdf": None, "Financials.xlsx": None},
    },
    "Downloads": {"picture1.jpg": None, "picture2.jpg": None},
}

print(list_files(test_input))