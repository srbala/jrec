#{{{ Marathon
from default import *
#}}} Marathon

from Modules import commonBits

def test():

    set_java_recorded_version("1.6.0_22")
    if frame(' - Open File:0'):
        select('File', commonBits.sampleXmlDir() + 'TestXml_01.xml')
        click('Edit')
    close()

    if window('Record Editor'):

        select_menu('File>>Export as CSV file')

 
        if frame('Export - TestXml_01.xml:0'):
            select('Edit Output File', 'true')
            select('Only export Nodes with Data', 'true')
            select('Add Quote to all Text Fields', 'true')
            select('Keep screen open', 'true')
            select('names on first line', 'true')
##            select('JTable_37', 'rows:[0],columns:[Include]')
            select('names on first line', 'true')
  ##          select('JTable_37', 'rows:[1],columns:[Include]')
            select('names on first line', 'true')
            click('save file')
        close()

        if frame('Table:  - TestXml_01.xml.csv:0'):
            assert_content('JTable_22', [ ['XML Start_Document', '', '', '', 'ISO-8859-1', '1.0'],
['XML Comment', '', '', '', ' Edited by XMLSpy\xae', ''],
['catalog', 'cd', 'title', 'Empire Burlesque', '', ''],
['catalog', 'cd', 'artist', 'Bob Dylan', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Columbia', '', ''],
['catalog', 'cd', 'price', '10.90', '', ''],
['catalog', 'cd', 'year', '1985', '', ''],
['catalog', 'cd', 'title', 'Hide your heart', '', ''],
['catalog', 'cd', 'artist', 'Bonnie Tyler', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'CBS Records', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1988', '', ''],
['catalog', 'cd', 'title', 'Greatest Hits', '', ''],
['catalog', 'cd', 'artist', 'Dolly Parton', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'RCA', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1982', '', ''],
['catalog', 'cd', 'title', 'Still got the blues', '', ''],
['catalog', 'cd', 'artist', 'Gary Moore', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Virgin records', '', ''],
['catalog', 'cd', 'price', '10.20', '', ''],
['catalog', 'cd', 'year', '1990', '', ''],
['catalog', 'cd', 'title', 'Eros', '', ''],
['catalog', 'cd', 'artist', 'Eros Ramazzotti', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'BMG', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1997', '', ''],
['catalog', 'cd', 'title', 'One night only', '', ''],
['catalog', 'cd', 'artist', 'Bee Gees', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Polydor', '', ''],
['catalog', 'cd', 'price', '10.90', '', ''],
['catalog', 'cd', 'year', '1998', '', ''],
['catalog', 'cd', 'title', 'Sylvias Mother', '', ''],
['catalog', 'cd', 'artist', 'Dr.Hook', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'CBS', '', ''],
['catalog', 'cd', 'price', '8.10', '', ''],
['catalog', 'cd', 'year', '1973', '', ''],
['catalog', 'cd', 'title', 'Maggie May', '', ''],
['catalog', 'cd', 'artist', 'Rod Stewart', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Pickwick', '', ''],
['catalog', 'cd', 'price', '8.50', '', ''],
['catalog', 'cd', 'year', '1990', '', ''],
['catalog', 'cd', 'title', 'Romanza', '', ''],
['catalog', 'cd', 'artist', 'Andrea Bocelli', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Polydor', '', ''],
['catalog', 'cd', 'price', '10.80', '', ''],
['catalog', 'cd', 'year', '1996', '', ''],
['catalog', 'cd', 'title', 'When a man loves a woman', '', ''],
['catalog', 'cd', 'artist', 'Percy Sledge', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Atlantic', '', ''],
['catalog', 'cd', 'price', '8.70', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', 'title', 'Black angel', '', ''],
['catalog', 'cd', 'artist', 'Savage Rose', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Mega', '', ''],
['catalog', 'cd', 'price', '10.90', '', ''],
['catalog', 'cd', 'year', '1995', '', ''],
['catalog', 'cd', 'title', '1999 Grammy Nominees', '', ''],
['catalog', 'cd', 'artist', 'Many', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Grammy', '', ''],
['catalog', 'cd', 'price', '10.20', '', ''],
['catalog', 'cd', 'year', '1999', '', ''],
['catalog', 'cd', 'title', 'For the good times', '', ''],
['catalog', 'cd', 'artist', 'Kenny Rogers', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Mucik Master', '', ''],
['catalog', 'cd', 'price', '8.70', '', ''],
['catalog', 'cd', 'year', '1995', '', ''],
['catalog', 'cd', 'title', 'Big Willie style', '', ''],
['catalog', 'cd', 'artist', 'Will Smith', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Columbia', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1997', '', ''],
['catalog', 'cd', 'title', 'Tupelo Honey', '', ''],
['catalog', 'cd', 'artist', 'Van Morrison', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Polydor', '', ''],
['catalog', 'cd', 'price', '8.20', '', ''],
['catalog', 'cd', 'year', '1971', '', ''],
['catalog', 'cd', 'title', 'Soulsville', '', ''],
['catalog', 'cd', 'artist', 'Jorn Hoel', '', ''],
['catalog', 'cd', 'country', 'Norway', '', ''],
['catalog', 'cd', 'company', 'WEA', '', ''],
['catalog', 'cd', 'price', '7.90', '', ''],
['catalog', 'cd', 'year', '1996', '', ''],
['catalog', 'cd', 'title', 'The very best of', '', ''],
['catalog', 'cd', 'artist', 'Cat Stevens', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Island', '', ''],
['catalog', 'cd', 'price', '8.90', '', ''],
['catalog', 'cd', 'year', '1990', '', ''],
['catalog', 'cd', 'title', 'Stop', '', ''],
['catalog', 'cd', 'artist', 'Sam Brown', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'A and M', '', ''],
['catalog', 'cd', 'price', '8.90', '', ''],
['catalog', 'cd', 'year', '1988', '', ''],
['catalog', 'cd', 'title', 'Bridge of Spies', '', ''],
['catalog', 'cd', 'artist', 'T`Pau', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Siren', '', ''],
['catalog', 'cd', 'price', '7.90', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', 'title', 'Private Dancer', '', ''],
['catalog', 'cd', 'artist', 'Tina Turner', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Capitol', '', ''],
['catalog', 'cd', 'price', '8.90', '', ''],
['catalog', 'cd', 'year', '1983', '', ''],
['catalog', 'cd', 'title', 'Midt om natten', '', ''],
['catalog', 'cd', 'artist', 'Kim Larsen', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Medley', '', ''],
['catalog', 'cd', 'price', '7.80', '', ''],
['catalog', 'cd', 'year', '1983', '', ''],
['catalog', 'cd', 'title', 'Pavarotti Gala Concert', '', ''],
['catalog', 'cd', 'artist', 'Luciano Pavarotti', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'DECCA', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1991', '', ''],
['catalog', 'cd', 'title', 'The dock of the bay', '', ''],
['catalog', 'cd', 'artist', 'Otis Redding', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Atlantic', '', ''],
['catalog', 'cd', 'price', '7.90', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', 'title', 'Picture book', '', ''],
['catalog', 'cd', 'artist', 'Simply Red', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Elektra', '', ''],
['catalog', 'cd', 'price', '7.20', '', ''],
['catalog', 'cd', 'year', '1985', '', ''],
['catalog', 'cd', 'title', 'Red', '', ''],
['catalog', 'cd', 'artist', 'The Communards', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'London', '', ''],
['catalog', 'cd', 'price', '7.80', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', 'title', 'Unchain my heart', '', ''],
['catalog', 'cd', 'artist', 'Joe Cocker', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'EMI', '', ''],
['catalog', 'cd', 'price', '8.20', '', ''],
['catalog', 'cd', 'year', '1987', '', '']
])
            select('JTable_22', 'rows:[0],columns:[2|Level_2]')
            select('JTable_27', 'rows:[6],columns:[Sl]')
        close()

        if frame('Table:  - TestXml_01.xml.csv:1'):
            select('JTable_22', 'rows:[6],columns:[2|Level_2]')
            select('JTable_27', 'rows:[6],columns:[Sl]')
        close()

        if frame('Record:  - TestXml_01.xml.csv:0'):
            assert_content('JTable_24', [ ['Level_1', '1', '', 'catalog', 'catalog'],
['Level_2', '2', '', 'cd', 'cd'],
['Level_3', '3', '', 'price', 'price'],
['Following~Text', '4', '', '10.90', '10.90'],
['Xml~Prefix', '5', '', '', ''],
['Xml~Namespace', '6', '', '', '']
])
            click('Close')
        close()

        if frame('Table:  - TestXml_01.xml.csv:0'):
            select('JTable_27', 'rows:[6],columns:[Sl]')
            select('JTable_27', 'rows:[6],columns:[Sl]')
            click('Close')
        close()

        if frame('Export - TestXml_01.xml:0'):
            select('Only export Nodes with Data', 'false')
            click('save file')
        close()

        if frame('Table:  - TestXml_01.xml.csv:0'):
            assert_content('JTable_22', [ ['', '', '', '', '', ''],
['XML Start_Document', '', '', '', 'ISO-8859-1', '1.0'],
['XML Comment', '', '', '', ' Edited by XMLSpy\xae', ''],
['catalog', '', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Empire Burlesque', '', ''],
['catalog', 'cd', 'artist', 'Bob Dylan', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Columbia', '', ''],
['catalog', 'cd', 'price', '10.90', '', ''],
['catalog', 'cd', 'year', '1985', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Hide your heart', '', ''],
['catalog', 'cd', 'artist', 'Bonnie Tyler', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'CBS Records', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1988', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Greatest Hits', '', ''],
['catalog', 'cd', 'artist', 'Dolly Parton', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'RCA', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1982', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Still got the blues', '', ''],
['catalog', 'cd', 'artist', 'Gary Moore', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Virgin records', '', ''],
['catalog', 'cd', 'price', '10.20', '', ''],
['catalog', 'cd', 'year', '1990', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Eros', '', ''],
['catalog', 'cd', 'artist', 'Eros Ramazzotti', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'BMG', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1997', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'One night only', '', ''],
['catalog', 'cd', 'artist', 'Bee Gees', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Polydor', '', ''],
['catalog', 'cd', 'price', '10.90', '', ''],
['catalog', 'cd', 'year', '1998', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Sylvias Mother', '', ''],
['catalog', 'cd', 'artist', 'Dr.Hook', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'CBS', '', ''],
['catalog', 'cd', 'price', '8.10', '', ''],
['catalog', 'cd', 'year', '1973', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Maggie May', '', ''],
['catalog', 'cd', 'artist', 'Rod Stewart', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Pickwick', '', ''],
['catalog', 'cd', 'price', '8.50', '', ''],
['catalog', 'cd', 'year', '1990', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Romanza', '', ''],
['catalog', 'cd', 'artist', 'Andrea Bocelli', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Polydor', '', ''],
['catalog', 'cd', 'price', '10.80', '', ''],
['catalog', 'cd', 'year', '1996', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'When a man loves a woman', '', ''],
['catalog', 'cd', 'artist', 'Percy Sledge', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Atlantic', '', ''],
['catalog', 'cd', 'price', '8.70', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Black angel', '', ''],
['catalog', 'cd', 'artist', 'Savage Rose', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Mega', '', ''],
['catalog', 'cd', 'price', '10.90', '', ''],
['catalog', 'cd', 'year', '1995', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', '1999 Grammy Nominees', '', ''],
['catalog', 'cd', 'artist', 'Many', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Grammy', '', ''],
['catalog', 'cd', 'price', '10.20', '', ''],
['catalog', 'cd', 'year', '1999', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'For the good times', '', ''],
['catalog', 'cd', 'artist', 'Kenny Rogers', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Mucik Master', '', ''],
['catalog', 'cd', 'price', '8.70', '', ''],
['catalog', 'cd', 'year', '1995', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Big Willie style', '', ''],
['catalog', 'cd', 'artist', 'Will Smith', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Columbia', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1997', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Tupelo Honey', '', ''],
['catalog', 'cd', 'artist', 'Van Morrison', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Polydor', '', ''],
['catalog', 'cd', 'price', '8.20', '', ''],
['catalog', 'cd', 'year', '1971', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Soulsville', '', ''],
['catalog', 'cd', 'artist', 'Jorn Hoel', '', ''],
['catalog', 'cd', 'country', 'Norway', '', ''],
['catalog', 'cd', 'company', 'WEA', '', ''],
['catalog', 'cd', 'price', '7.90', '', ''],
['catalog', 'cd', 'year', '1996', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'The very best of', '', ''],
['catalog', 'cd', 'artist', 'Cat Stevens', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Island', '', ''],
['catalog', 'cd', 'price', '8.90', '', ''],
['catalog', 'cd', 'year', '1990', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Stop', '', ''],
['catalog', 'cd', 'artist', 'Sam Brown', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'A and M', '', ''],
['catalog', 'cd', 'price', '8.90', '', ''],
['catalog', 'cd', 'year', '1988', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Bridge of Spies', '', ''],
['catalog', 'cd', 'artist', 'T`Pau', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Siren', '', ''],
['catalog', 'cd', 'price', '7.90', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Private Dancer', '', ''],
['catalog', 'cd', 'artist', 'Tina Turner', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'Capitol', '', ''],
['catalog', 'cd', 'price', '8.90', '', ''],
['catalog', 'cd', 'year', '1983', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Midt om natten', '', ''],
['catalog', 'cd', 'artist', 'Kim Larsen', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Medley', '', ''],
['catalog', 'cd', 'price', '7.80', '', ''],
['catalog', 'cd', 'year', '1983', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Pavarotti Gala Concert', '', ''],
['catalog', 'cd', 'artist', 'Luciano Pavarotti', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'DECCA', '', ''],
['catalog', 'cd', 'price', '9.90', '', ''],
['catalog', 'cd', 'year', '1991', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'The dock of the bay', '', ''],
['catalog', 'cd', 'artist', 'Otis Redding', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'Atlantic', '', ''],
['catalog', 'cd', 'price', '7.90', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Picture book', '', ''],
['catalog', 'cd', 'artist', 'Simply Red', '', ''],
['catalog', 'cd', 'country', 'EU', '', ''],
['catalog', 'cd', 'company', 'Elektra', '', ''],
['catalog', 'cd', 'price', '7.20', '', ''],
['catalog', 'cd', 'year', '1985', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Red', '', ''],
['catalog', 'cd', 'artist', 'The Communards', '', ''],
['catalog', 'cd', 'country', 'UK', '', ''],
['catalog', 'cd', 'company', 'London', '', ''],
['catalog', 'cd', 'price', '7.80', '', ''],
['catalog', 'cd', 'year', '1987', '', ''],
['catalog', 'cd', '', '', '', ''],
['', '', '', '', '', ''],
['catalog', 'cd', 'title', 'Unchain my heart', '', ''],
['catalog', 'cd', 'artist', 'Joe Cocker', '', ''],
['catalog', 'cd', 'country', 'USA', '', ''],
['catalog', 'cd', 'company', 'EMI', '', ''],
['catalog', 'cd', 'price', '8.20', '', ''],
['catalog', 'cd', 'year', '1987', '', '']
])
            select('JTable_22', 'rows:[0],columns:[2|Level_2]')
            select('JTable_27', 'rows:[4],columns:[Sl]')
        close()

        if frame('Table:  - TestXml_01.xml.csv:1'):
            select('JTable_22', 'rows:[4],columns:[2|Level_2]')
            select('JTable_27', 'rows:[4],columns:[Sl]')
        close()

        if frame('Record:  - TestXml_01.xml.csv:0'):
            click('Close')
        close()

        if frame('Table:  - TestXml_01.xml.csv:0'):
            select('JTable_27', 'rows:[4],columns:[Sl]')
            select('JTable_27', 'rows:[4],columns:[Sl]')
            click('Close')
        close()

        if frame('Export - TestXml_01.xml:0'):
            click('Close')
        close()

 ##       window_closed('Record Editor')
    close()

    pass
