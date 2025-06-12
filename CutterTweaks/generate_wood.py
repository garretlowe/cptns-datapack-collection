import json

wood_map = {
	'minecraft': {
		'woods': ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry', 'pale_oak'],
		'stems': ['crimson', 'warped'],
		'blocks': ['bamboo']
	},
}

def write_file(from_block, to_block, count, namespace='minecraft'):
	new_json = {
		"type": f"minecraft:stonecutting",
		"ingredient": f"{namespace}:{from_block}",
		"result": {
			"id": f"{namespace}:{to_block}",
			"count": count
		}
	}
	
	OUTPUT_DIR = f'./{namespace}/data/cptnjtk/recipe/'
	with open(OUTPUT_DIR + f"{to_block}_from_{from_block}_stonecutting.json", 'w') as file:
		json.dump(new_json, file, indent=4)

def generate_recipes(namespace: str, namespace_items: dict):
	for wood in namespace_items['woods']:
		# Planks
		write_file(f"{wood}_planks", f"{wood}_stairs", 1, namespace)
		write_file(f"{wood}_planks", f"{wood}_slab", 2, namespace)
		write_file(f"{wood}_planks", f"{wood}_fence", 1, namespace)
		write_file(f"{wood}_planks", f"{wood}_fence_gate", 1, namespace)

		# Wood
		write_file(f"{wood}_wood", f"{wood}_planks", 4, namespace)
		write_file(f"{wood}_wood", f"stripped_{wood}_wood", 1, namespace)
		write_file(f"{wood}_wood", f"{wood}_log", 1, namespace)

		# Stripped Wood
		write_file(f"stripped_{wood}_wood", f"{wood}_planks", 4, namespace)
		write_file(f"stripped_{wood}_wood", f"stripped_{wood}_log", 1, namespace)

		# Logs
		write_file(f"{wood}_log", f"{wood}_planks", 4, namespace)
		write_file(f"{wood}_log", f"stripped_{wood}_log", 1, namespace)
		write_file(f"{wood}_log", f"{wood}_wood", 1, namespace)

		# Stripped Logs
		write_file(f"stripped_{wood}_log", f"{wood}_planks", 4, namespace)
		write_file(f"stripped_{wood}_log", f"stripped_{wood}_wood", 1, namespace)

	for stem in namespace_items['stems']:
		# Planks
		write_file(f"{stem}_planks", f"{stem}_stairs", 1, namespace)
		write_file(f"{stem}_planks", f"{stem}_slab", 2, namespace)
		write_file(f"{stem}_planks", f"{stem}_fence", 1, namespace)
		write_file(f"{stem}_planks", f"{stem}_fence_gate", 1, namespace)

		# Hyphae
		write_file(f"{stem}_hyphae", f"{stem}_planks", 4, namespace)
		write_file(f"{stem}_hyphae", f"stripped_{stem}_hyphae", 1, namespace)
		write_file(f"{stem}_hyphae", f"{stem}_stem", 1, namespace)

		# Stripped Hyphae
		write_file(f"stripped_{stem}_hyphae", f"{stem}_planks", 4, namespace)
		write_file(f"stripped_{stem}_hyphae", f"stripped_{stem}_stem", 1, namespace)

		# Stems
		write_file(f"{stem}_stem", f"{stem}_planks", 4, namespace)
		write_file(f"{stem}_stem", f"stripped_{stem}_stem", 1, namespace)
		write_file(f"{stem}_stem", f"{stem}_hyphae", 1, namespace)

		# Stripped Stems
		write_file(f"stripped_{stem}_stem", f"{stem}_planks", 4, namespace)
		write_file(f"stripped_{stem}_stem", f"stripped_{stem}_hyphae", 1, namespace)

	for block in namespace_items['blocks']:
		# Planks
		write_file(f"{block}_planks", f"{block}_stairs", 1, namespace)
		write_file(f"{block}_planks", f"{block}_slab", 2, namespace)
		write_file(f"{block}_planks", f"{block}_fence", 1, namespace)
		write_file(f"{block}_planks", f"{block}_fence_gate", 1, namespace)

		# Blocks
		write_file(f"{block}_block", f"{block}_planks", 2, namespace)
		write_file(f"{block}_block", f"stripped_{block}_block", 1, namespace)

		# Stripped Blocks
		write_file(f"stripped_{block}_block", f"{block}_planks", 2, namespace)

def main():
	for namespace in wood_map:
		generate_recipes(namespace, wood_map[namespace])

main()
