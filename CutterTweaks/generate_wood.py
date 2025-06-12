import json

wood_map = {
	'minecraft': {
		'woods': ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry', 'pale_oak'],
		'stems': ['crimson', 'warped'],
		'blocks': ['bamboo'],
		'exceptions': {}
	},
	# 'betterdefaultbiomes': {
	# 	'woods': [],
	# 	'stems': [],
	# 	'blocks': [],
	# 	'exceptions': {
	# 		'palm': {
	# 			'item_type': 'wood',
	# 			'replacements': [{
	# 				'from_prefix': 'stripped_',
	# 				'from_suffix': 'log',
	# 				'to_prefix': '',
	# 				'to_suffix': 'log_stripped'
	# 			},
	# 			{
	# 				'from_prefix': 'stripped_',
	# 				'from_suffix': 'wood',
	# 				'to_prefix': '',
	# 				'to_suffix': 'wood_stripped'
	# 			}]
	# 		},
	# 		'swamp_willow': {
	# 			'item_type': 'wood',
	# 			'replacements': [{
	# 				'from_prefix': 'stripped_',
	# 				'from_suffix': 'log',
	# 				'to_prefix': '',
	# 				'to_suffix': 'log_stripped'
	# 			},
	# 			{
	# 				'from_prefix': 'stripped_',
	# 				'from_suffix': 'wood',
	# 				'to_prefix': '',
	# 				'to_suffix': 'wood_stripped'
	# 			}]
	# 		}
	# 	}
	# },
	# 'biomesoplenty': {
	# 	'woods': ['fir', 'redwood', 'cherry', 'mahogany', 'jacaranda', 'palm', 'willow', 'dead', 'magic', 'umbran', 'hellbark'],
	# 	'stems': [],
	# 	'blocks': [],
	# 	'exceptions': {}
	# },
	# 'blue_skies': {
	# 	'woods': ['bluebright', 'starlit', 'frostbright', 'lunar', 'dusk', 'maple', 'cherry'],
	# 	'stems': [],
	# 	'blocks': [],
	# 	'exceptions': {
	# 		'crystallized': {
	# 			'item_type': 'wood',
	# 			'replacements': [{
	# 				'from_prefix': '',
	# 				'from_suffix': 'fence',
	# 				'to_prefix': '',
	# 				'to_suffix': 'wall'
	# 			}]
	# 		}
	# 	}
	# },
	# 'byg': {
	# 	'woods': ['aspen', 'baobab', 'blue_enchanted', 'cherry', 'cika', 'cypress', 'ebony', 'ether', 'fir', 'green_enchanted', 'holly', 'jacaranda', 'lament', 'mahogany', 'mangrove', 'maple', 'nightshade', 'palm', 'palo_verde', 'pine', 'rainbow_eucalyptus', 'redwood', 'skyris', 'willow', 'witch_hazel', 'zelkova'],
	# 	'stems': ['imparius', 'fungal_imparius', 'synthian'],
	# 	'blocks': [],
	# 	'exceptions': {
	# 		'embur': {
	# 			'item_type': 'stem',
	# 			'replacements': [{
	# 				'from_prefix': '',
	# 				'from_suffix': 'stem',
	# 				'to_prefix': '',
	# 				'to_suffix': 'pedu'
	# 			},
	# 			{
	# 				'from_prefix': 'stripped_',
	# 				'from_suffix': 'stem',
	# 				'to_prefix': 'stripped_',
	# 				'to_suffix': 'pedu'
	# 			}]
	# 		},
	# 		'bulbis': {
	# 			'item_type': 'stem',
	# 			'replacements': [{
	# 				'from_prefix': '',
	# 				'from_suffix': 'hyphae',
	# 				'to_prefix': '',
	# 				'to_suffix': 'wood'
	# 			},
	# 			{
	# 				'from_prefix': 'stripped_',
	# 				'from_suffix': 'hyphae',
	# 				'to_prefix': 'stripped_',
	# 				'to_suffix': 'wood'
	# 			}]
	# 		}
	# 	}
	# },
	# 'twilightforest': {
	# 	'woods': ['twilight_oak', 'canopy', 'mangrove', 'dark', 'time', 'transformation', 'mining', 'sorting'],
	# 	'stems': [],
	# 	'blocks': [],
	# 	'exceptions': {}
	# }
}

def exception_string(block_name, expected_prefix, expected_suffix, exceptions):
	out_str = f"{expected_prefix}{block_name}_{expected_suffix}"


	if block_name in exceptions:
		exception = [exception for exception in exceptions[block_name]['replacements'] if exception['from_prefix'] == expected_prefix and exception['from_suffix'] == expected_suffix]
		if len(exception) != 0:
			out_str = f"{exception[0]['to_prefix']}{block_name}_{exception[0]['to_suffix']}"
	return out_str

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
	with open(OUTPUT_DIR + f"{f'{namespace}_' if namespace != 'minecraft' else ''}{to_block}_from_{from_block}_stonecutting.json", 'w') as file:
		json.dump(new_json, file, indent=4)

def generate_wood_recipes(namespace: str, wood: str, exceptions=None):
	plank_str = exception_string(wood, '', 'planks', exceptions)
	stairs_str = exception_string(wood, '', 'stairs', exceptions)
	slab_str = exception_string(wood, '', 'slab', exceptions)
	fence_str = exception_string(wood, '', 'fence', exceptions)
	fence_gate_str = exception_string(wood, '', 'fence_gate', exceptions)
	wood_str = exception_string(wood, '', 'wood', exceptions)
	stripped_wood_str = exception_string(wood, 'stripped_', 'wood', exceptions)
	log_str = exception_string(wood, '', 'log', exceptions)
	stripped_log_str = exception_string(wood, 'stripped_', 'log', exceptions)

	# Planks
	write_file(plank_str, stairs_str, 1, namespace)
	write_file(plank_str, slab_str, 2, namespace)
	write_file(plank_str, fence_str, 1, namespace)
	write_file(plank_str, fence_gate_str, 1, namespace)

	# Wood
	write_file(wood_str, plank_str, 4, namespace)
	write_file(wood_str, stripped_wood_str, 1, namespace)
	write_file(wood_str, log_str, 1, namespace)

	# Stripped Wood
	write_file(stripped_wood_str, plank_str, 4, namespace)
	write_file(stripped_wood_str, stripped_log_str, 1, namespace)

	# Logs
	write_file(log_str, plank_str, 4, namespace)
	write_file(log_str, stripped_log_str, 1, namespace)
	write_file(log_str, wood_str, 1, namespace)

	# Stripped Logs
	write_file(stripped_log_str, plank_str, 4, namespace)
	write_file(stripped_log_str, stripped_wood_str, 1, namespace)

def generate_stem_recipes(namespace:str, stem: str, exceptions: dict):
	plank_str = exception_string(stem, '', 'planks', exceptions)
	stairs_str = exception_string(stem, '', 'stairs', exceptions)
	slab_str = exception_string(stem, '', 'slab', exceptions)
	fence_str = exception_string(stem, '', 'fence', exceptions)
	fence_gate_str = exception_string(stem, '', 'fence_gate', exceptions)
	hyphae_str = exception_string(stem, '', 'hyphae', exceptions)
	stripped_hyphae_str = exception_string(stem, 'stripped_', 'hyphae', exceptions)
	stem_str = exception_string(stem, '', 'stem', exceptions)
	stripped_stem_str = exception_string(stem, 'stripped_', 'stem', exceptions)

	# Planks
	write_file(plank_str, stairs_str, 1, namespace)
	write_file(plank_str, slab_str, 2, namespace)
	write_file(plank_str, fence_str, 1, namespace)
	write_file(plank_str, fence_gate_str, 1, namespace)

	# Hyphae
	write_file(hyphae_str, plank_str, 4, namespace)
	write_file(hyphae_str, stripped_hyphae_str, 1, namespace)
	write_file(hyphae_str, stem_str, 1, namespace)

	# Stripped Hyphae
	write_file(stripped_hyphae_str, plank_str, 4, namespace)
	write_file(stripped_hyphae_str, stripped_stem_str, 1, namespace)

	# Stems
	write_file(stem_str, plank_str, 4, namespace)
	write_file(stem_str, stripped_stem_str, 1, namespace)
	write_file(stem_str, hyphae_str, 1, namespace)

	# Stripped Stems
	write_file(stripped_stem_str, plank_str, 4, namespace)
	write_file(stripped_stem_str, stripped_hyphae_str, 1, namespace)

def generate_block_recipes(namespace: str, block: str, exceptions: dict):
	plank_str = exception_string(block, '', 'planks', exceptions)
	stairs_str = exception_string(block, '', 'stairs', exceptions)
	slab_str = exception_string(block, '', 'slab', exceptions)
	fence_str = exception_string(block, '', 'fence', exceptions)
	fence_gate_str = exception_string(block, '', 'fence_gate', exceptions)
	block_str = exception_string(block, '', 'block', exceptions)
	stripped_block_str = exception_string(block, 'stripped_', 'block', exceptions)

	# Planks
	write_file(plank_str, stairs_str, 1, namespace)
	write_file(plank_str, slab_str, 2, namespace)
	write_file(plank_str, fence_str, 1, namespace)
	write_file(plank_str, fence_gate_str, 1, namespace)

	# Blocks
	write_file(block_str, plank_str, 2, namespace)
	write_file(block_str, stripped_block_str, 1, namespace)

	# Stripped Blocks
	write_file(stripped_block_str, plank_str, 2, namespace)

def get_exceptions_for_item_type(exceptions: dict, item_type: str):
	return { block_name: block_exceptions for block_name, block_exceptions in exceptions.items() if block_exceptions['item_type'] == item_type }

def generate_recipes(namespace: str, namespace_items: dict):
	exceptions = namespace_items['exceptions']

	wood_exceptions = get_exceptions_for_item_type(exceptions, 'wood')
	for wood in (namespace_items['woods'] + list(wood_exceptions.keys())):
		generate_wood_recipes(namespace, wood, wood_exceptions)

	stem_exceptions = get_exceptions_for_item_type(exceptions, 'stem')
	for stem in (namespace_items['stems'] + list(stem_exceptions.keys())):
		generate_stem_recipes(namespace, stem, stem_exceptions)
	
	block_exceptions = get_exceptions_for_item_type(exceptions, 'block')
	for block in (namespace_items['blocks'] + list(block_exceptions.keys())):
		generate_block_recipes(namespace, block, block_exceptions)

def main():
	for namespace in wood_map:
		generate_recipes(namespace, wood_map[namespace])

main()
