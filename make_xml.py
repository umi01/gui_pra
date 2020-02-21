import xml.etree.ElementTree as ET

def make_xml(dc):

    #XML文字列の生成
    roots = ET.Element('root', {'ttl':'test_root'})
    p = ET.SubElement(roots, 'p1') 
    t = ET.SubElement(p, 'fld1', {'atr1':'1.1','atr2':'1.5'}) 
    t.text = dc["fld1"] 
    t = ET.SubElement(p, 'fld2', {'atr1':'2.2','atr2':'2.5'}) 
    t.text = dc["fld2"] 
    p = ET.SubElement(roots, 'p3') 
    t = ET.SubElement(p, 'fld3', {'atr1':'3.3','atr2':'3.5'}) 
    t.text = dc["fld3"] 

    #XML文字列の出力
    ET.dump(roots)

    #XMLファイルの生成
    tree = ET.ElementTree(roots) 
    fl = 'test.xml'  
    tree.write(fl)

    # 生成したXMLファイル名を返す
    return fl 

def read_xml(fl):
    tree = ET.parse(fl) 
    root = tree.getroot() 

    #tg  = root.tag
    #atr = root.attrib

    for c1 in root:
        print(c1.tag)
        for c2 in c1:
            tg = c2.tag
            atr1 = c2.attrib.get("atr1") 
            atr2 = c2.attrib.get("atr2") 
            txt  = c2.text
            print(atr1,atr2,txt)

# main
if __name__ == '__main__':

      #引数で渡すダミーの辞書
      dc = {'fld1': 'test1', 'fld2': 'test2', 'fld3': 'test3'}

      #print(dc)
      #print(dc["fld1"])

      # XMLファイルの生成
      fl = make_xml(dc)                        
      print( fl )

      # XMLファイルの読み込み
      read_xml( fl )   