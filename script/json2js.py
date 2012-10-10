def json2js(jsonfile, jsfile):
    open(jsfile, 'w').write("offload(%s);" % (open(jsonfile).read()))

if __name__=='__main__':
    import sys
    for jsonfile in sys.argv[1:]:
        json2js(jsonfile, jsonfile.replace('.json', '.js'))
