#{{{ Marathon
from default import *
#}}} Marathon

from Modules import commonBits

def test():

    set_java_recorded_version("1.6.0_22")
    if frame(' - Open File:0'):
        select('File', commonBits.sampleDir() + 'DTAR020_tst1.bin')
        click('Edit')
    close()

    if window('Record Editor'):
        select_menu('Utilities>>Run Script>>Hello.js')

        if window('Message'):
            assert_p('OptionPane.button', 'Text', 'OK')
            assert_p('OptionPane.label', 'Text', 'Hello, world!')
            click('OptionPane.button')
        close()

        if frame('Table:  - DTAR020_tst1.bin:0'):
            click('Close')
        close()

    close()

    pass
