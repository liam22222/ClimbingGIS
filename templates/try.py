import json
# # list = """Technion Crag: ['35.013406', '32.778895']
# # Mearat Hanezirim: ['34.972004', '31.926599']
# # Kebara Crag: ['34.937115', '32.563702']
# # Gilboa Gefet Cliff: ['35.418005', '32.494922']
# # Dalton: ['35.510623', '33.006648']
# # Vanishing Cliff: ['35.563688', '33.190917']
# # Haavot Crag: ['35.136093', '31.670552']
# # The Oaks Crag: ['35.555121', '33.163927']
# # המצוק הנעלם: ['35.564353', '33.190863']
# # Mukhraka: ['35.092049', '32.688636']
# # Giladi: ['35.562015', '33.245148']
# # Halilim: ['35.16387', '31.804296']
# # Amir Kra: ['35.548488', '33.197238']
# # The Oil Crag: ['35.691855', '33.16885']
# # Ramim Ridge: ['35.549987', '33.192069']
# # The Grand Crag: ['35.00832', '32.78753']
# # Ein Carem Cliff: ['35.162687', '31.760666']
# # Arava Crag: ['35.297003', '30.971132']
# # Gey Ben Hinom: ['35.286884', '31.765537']
# # Nir: ['35.550427', '33.187313']"""
# # for line in list.split('\n'):
# #     line = line.split(':')
# #     name = line[0]
# #     line = line[1]
# #     line = line[2:-1]
# #     line = line.split(', ')
# #     lag, lan = line[0], line[1]
# #     lag, lan = lag[1:-1], lan[1:-1]
# #     my_dict = {
# #           "type": "Feature",
# #           "properties": {
# #             "name": name,
# #             "color": "#3001CE"
# #           },
# #           "geometry": {
# #             "type": "Point",
# #             "coordinates": [
# #               float(lag),
# #               float(lan)
# #             ]
# #           }
# #     }
# #     print(f'{my_dict},')
# text = """{'type': 'Feature', 'properties': {'name': 'Technion Crag', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.013406, 32.778895]}},
# {'type': 'Feature', 'properties': {'name': 'Mearat Hanezirim', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [34.972004, 31.926599]}},
# {'type': 'Feature', 'properties': {'name': 'Kebara Crag', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [34.937115, 32.563702]}},
# {'type': 'Feature', 'properties': {'name': 'Gilboa Gefet Cliff', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.418005, 32.494922]}},
# {'type': 'Feature', 'properties': {'name': 'Dalton', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.510623, 33.006648]}},
# {'type': 'Feature', 'properties': {'name': 'Vanishing Cliff', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.563688, 33.190917]}},
# {'type': 'Feature', 'properties': {'name': 'Haavot Crag', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.136093, 31.670552]}},
# {'type': 'Feature', 'properties': {'name': 'The Oaks Crag', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.555121, 33.163927]}},
# {'type': 'Feature', 'properties': {'name': 'המצוק הנעלם', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.564353, 33.190863]}},
# {'type': 'Feature', 'properties': {'name': 'Mukhraka', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.092049, 32.688636]}},
# {'type': 'Feature', 'properties': {'name': 'Giladi', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.562015, 33.245148]}},
# {'type': 'Feature', 'properties': {'name': 'Halilim', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.16387, 31.804296]}},
# {'type': 'Feature', 'properties': {'name': 'Amir Kra', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.548488, 33.197238]}},
# {'type': 'Feature', 'properties': {'name': 'The Oil Crag', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.691855, 33.16885]}},
# {'type': 'Feature', 'properties': {'name': 'Ramim Ridge', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.549987, 33.192069]}},
# {'type': 'Feature', 'properties': {'name': 'The Grand Crag', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.00832, 32.78753]}},
# {'type': 'Feature', 'properties': {'name': 'Ein Carem Cliff', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.162687, 31.760666]}},
# {'type': 'Feature', 'properties': {'name': 'Arava Crag', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.297003, 30.971132]}},
# {'type': 'Feature', 'properties': {'name': 'Gey Ben Hinom', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.286884, 31.765537]}},
# {'type': 'Feature', 'properties': {'name': 'Nir', 'color': '#3001CE'}, 'geometry': {'type': 'Point', 'coordinates': [35.550427, 33.187313]}}"""
# print(text.replace("'", '"'))

liam = b'{"name": "liam"}'
print(liam, type(liam))
liam = json.loads(liam)
print(liam, type(liam))