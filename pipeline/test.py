import os

# def find_file(folder, filename):
#     """Search for a file within a folder and print relative path."""
#     for root, dirs, files in os.walk(folder):
#         if filename in files:
#             relative_path = os.path.relpath(root, start=folder)
#             print(f"File found: {filename} in folder: {relative_path or '.'}")
#             return os.path.join(root, filename)
#     print(f"File '{filename}' not found in '{folder}'.")
#     return None

# # Example usage
# folder = "data"  # Specify the folder to search in
# filename = "customer_stats.parquet"  # Specify the file to find

# print(find_file(folder, filename))


# current_dir = os.path.dirname(os.path.abspath(__file__))
# root_dir = os.path.dirname(current_dir)
# feature_store_path = os.path.join(root_dir, "feature_store", "feature_store.yaml") 

# print(feature_store_path)