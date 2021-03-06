/*
 * @Author Bruce Martin
 * Created on 20/03/2007
 *
 * Purpose:
 */
package net.sf.RecordEditor.re.editProperties;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;

import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JEditorPane;

import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.params.Parameters;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.treeCombo.JarFileSelect;

/**
 *
 *
 * @author Bruce Martin
 *
 */
@SuppressWarnings("serial")
public class EditIcons extends BasePanel implements ActionListener {

    private static final String DESCRIPTION
    	= LangConversion.convertId(LangConversion.ST_MESSAGE, "EditProperties_Icons",
    			  "<h2>Icons</h2>"
    			+ "This screen lets you choose which icon set to use in the <b>RecordEditor</b>");
    private static final String[] ICON_NAMES = {
            "Windows",
            "Eclipse",
            "Office XP",
            "Office 2003",
            "Aqua",
            "Gnome",
            "Tango",
            "Other"
    };
    private static final String[] ZIP_NAME = {
            "",
            "<lib>/iconsEclipse.zip",
            "<lib>/iconsOfficeXP.zip",
            "<lib>/iconsOffice2003.zip",
            "<lib>/iconsAqua.zip",
            "<lib>/iconsGnome.zip",
            "<lib>/iconsTango.zip",
            ""
    };
    private static final boolean[] USE_PNG = {
            true,
            false,
            false,
            false,
            true,
            true,
            true,
            false
    };

    private static final int OTHER_ZIP_OPTION = ICON_NAMES.length - 1;

    private JEditorPane tips = new JEditorPane("text/html", DESCRIPTION);

    private JComboBox looks  = new JComboBox(ICON_NAMES);
    private JCheckBox usePng = new JCheckBox();
    private JarFileSelect jarName  = new JarFileSelect(true, null);

    private EditParams pgmParams;


    /**
     * Edit Icons to be displayed
     * @param params program parameters
     */
    public EditIcons(final EditParams params) {
        super();

        pgmParams = params;

        init_100_ScreenFields();
        init_200_ScreenBuild();
    }


    /**
     * Initialise / setup screen fields
     *
     */
    private void init_100_ScreenFields() {
        String usePgnStr = pgmParams.getProperty(Parameters.PROPERTY_PGN_ICONS, "Y").toUpperCase();
        FocusAdapter focusMgr = new FocusAdapter() {
            public void focusLost(FocusEvent e) {
                setParameters();
            }
        };

        looks.setSelectedIndex(0);
        try {
            int idx = Integer.parseInt(
                    pgmParams.getProperty(Parameters.PROPERTY_ICON_INDEX));
            looks.setSelectedIndex(idx);
        } catch (Exception e) {
        }
        usePng.setSelected("Y".equals(usePgnStr));
        jarName.setText(pgmParams.iconJar);

        setOptions();


        usePng.addActionListener(this);
        looks.addActionListener(this);
        looks.addFocusListener(focusMgr);
        jarName.addFcFocusListener(focusMgr);
    }

    /**
     * Setup the screen
     *
     */
    private void init_200_ScreenBuild() {

		this.addComponentRE(1, 5, CommonCode.TIP_HEIGHT, BasePanel.GAP2,
		        BasePanel.FULL, BasePanel.FULL,
				tips);

        this.addLineRE("Icon Set", looks);
        this.setGapRE(BasePanel.GAP1);
		this.addLineRE("Look for png icons", usePng);
        this.setGapRE(BasePanel.GAP1);

        this.addLineRE("Zip/Jar File", jarName); 
    }

    /**
     * Update fields after for the current combo Box
     *
     */
    private void setOptions() {
        int idx = looks.getSelectedIndex();
        boolean otherOption = idx == OTHER_ZIP_OPTION;

        if (! otherOption) {
            jarName.setText(ZIP_NAME[idx]);
        }
        if (idx < OTHER_ZIP_OPTION) {
            usePng.setSelected(USE_PNG[idx]);
        }
        usePng.setEnabled(otherOption);
        jarName.setEnabled(otherOption);
    }

    /**
     * Save the updated parameters
     *
     */
    private void setParameters() {
        String usePgnString = "N";

        if (usePng.isSelected()) {
            usePgnString = "Y";
        }

        pgmParams.setProperty(Parameters.PROPERTY_ICON_INDEX,
                			  Integer.toString(looks.getSelectedIndex()));
        pgmParams.setProperty(Parameters.PROPERTY_PGN_ICONS, usePgnString);

        pgmParams.iconJar = jarName.getText();
    }

    /**
     * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
     */
    public final void actionPerformed(ActionEvent e) {

        setOptions();
        setParameters();
    }
}
