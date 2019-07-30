import urllib3

reply = urllib3.PoolManager().request('GET','http://overpass-api.de/api/interpreter?data=node(44,22,44.1,22.1);way(44,22,44.005,22.005);relation(44,22,44.005,22.005);out%20meta;')
#print(reply.data.decode())
with open('somefile.xml', 'w', encoding='utf-8') as osm_data_xml:
    for line in reply.data.decode().splitlines():
        osm_data_xml.writelines(line+"\n")