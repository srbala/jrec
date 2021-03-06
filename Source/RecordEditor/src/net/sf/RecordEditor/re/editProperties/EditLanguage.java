package net.sf.RecordEditor.re.editProperties;

import java.awt.Component;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.io.File;
import java.util.Locale;
import java.util.TreeMap;
import java.util.TreeSet;

import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JEditorPane;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.ListCellRenderer;

import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.params.Parameters;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.treeCombo.TreeComboFileSelect;

/**
 * Purpose: Change the foreign language used in the RecordEditor
 * License: GPL
 *
 * @author Bruce Martin
 *
 */
@SuppressWarnings("serial")
public class EditLanguage extends BasePanel {

	private static final String FLAG_DIR = "/pict/flags/";
	private static final ImageIcon BLANK_ICON =  Common.readIcon(FLAG_DIR + "blank.png");

	private static final String DESCRIPTION
		= LangConversion.convertId(LangConversion.ST_MESSAGE, "EditProtoperties_Language",
				  "<h2>Foreign Language</h2>"
				+ "This screen lets you change the language used in the <b>RecordEditor</b><br/>"
				+ "You will need to <b>exit</b> and <b>restart</b> the Editor for the change to come into effect<br/><br/>"
				+ "If your language is not supported ???, Why not do the Translation your self ???.<br/>"
				+ "Have a look at the ReadMe.html in the language directory:")
				+ " " + Parameters.expandVars(
							Parameters.formatLangDir(
									Parameters.getString(Parameters.LANG_DIRECTORY)));

	private JEditorPane tips = new JEditorPane("text/html", DESCRIPTION);

	private TreeComboFileSelect langDirFchooser = new TreeComboFileSelect(true, false, true, null, null);

	private JComboBox languagesCombo = new JComboBox();

	private final EditParams params;

	private String lastLangDir = null,
		           lastLang ;

	private TreeMap<String, FlagComboItem> langItmHash = new TreeMap<String, EditLanguage.FlagComboItem>();
	private TreeMap<String, String> langLongName = new TreeMap<String, String>();


   public EditLanguage(final EditParams params) {
	   this.params = params;

	   init_100_InitVars();
	   init_200_LayoutScreen();
	   init_300_FinaliseScreen();
   }

   private void init_100_InitVars() {
	   init_110_InitLang();
	   lastLang = params.getProperty(Parameters.CURRENT_LANGUAGE);
//	   languagesCombo.setSelectedItem(params.getProperty(Parameters.CURRENT_LANGUAGE));
//	   System.out.println("@@ " + languagesCombo.getSelectedItem()
//			   + " " + params.getProperty(Parameters.CURRENT_LANGUAGE));
	   getLanguages();

	   langDirFchooser.setText(getLangDir());
	   langDirFchooser.setExpandVars(true);
//	   langDirFchooser.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);

	   if (lastLang != null && langItmHash.containsKey(lastLang)) {
		   languagesCombo.setSelectedItem(langItmHash.get(lastLang));
	   } else {
		   languagesCombo.setSelectedIndex(0);
	   }

   }

   private void init_110_InitLang() {
		Locale[] locales = Locale.getAvailableLocales();
		String s;


		for (Locale l : locales) {
			s = l.getCountry();

			if (s != null && ! "".equals(s)) {
				langLongName.put(s.toLowerCase(), l.getDisplayLanguage());
			}
		}

		for (Locale l : locales) {
			langLongName.put(l.getLanguage(), l.getDisplayLanguage());
		}

   }

   private void init_200_LayoutScreen() {

	   this.addComponentRE(1, 5, CommonCode.TIP_HEIGHT, BasePanel.GAP2,
		        BasePanel.FULL, BasePanel.FULL,
				tips);
	   this.addLineRE("Language Directory", langDirFchooser);
	   this.addLineRE("Language", languagesCombo);
   }

   private void init_300_FinaliseScreen() {

	   languagesCombo.setRenderer(new FlagComboRenderer());
	   langDirFchooser.addFcFocusListener(new FocusAdapter() {

			/* (non-Javadoc)
			 * @see java.awt.event.FocusAdapter#focusLost(java.awt.event.FocusEvent)
			 */
			@Override
			public void focusLost(FocusEvent e) {

				params.setProperty(
						Parameters.LANG_DIRECTORY,
						langDirFchooser.getText());
				params.propertiesChanged = true;

				//lastLangDir = langDirFchooser.getText();
				System.out.println("Focus Lost ... get Languages");
				getLanguages();
			}
	   });

	   languagesCombo.addFocusListener(new FocusAdapter() {

			/* (non-Javadoc)
			 * @see java.awt.event.FocusAdapter#focusLost(java.awt.event.FocusEvent)
			 */
			@Override
			public void focusLost(FocusEvent e) {
				Object o = languagesCombo.getSelectedItem();
				if (o == null) {
					o = "";
				}

				lastLang = o.toString().trim();
				params.setProperty(
						Parameters.CURRENT_LANGUAGE,
						lastLang);
				params.propertiesChanged = true;
			}
	   });
   }


   private void getLanguages() {

	   String dir = Parameters.expandVars(getLangDir());

	   if (lastLangDir == null || ! lastLangDir.equals(dir)) {
		   String s;
		   String langFilePref = "ReMsgs.";
		   Object lang = languagesCombo.getSelectedItem();
		   TreeSet<String> items = new TreeSet<String>();

		   lastLangDir = dir;
		   languagesCombo.removeAllItems();
		   langItmHash.clear();

		   File directory = new File(dir);
		   ImageIcon flag;

		   if (directory.exists() && directory.isDirectory()) {
			   File[] fList = directory.listFiles();

			   for (File file : fList) {
				   if (file.isFile()) {
					   s = file.getName();
					   if (s.startsWith(Parameters.LANG_FILE_PREFIX)) {
						   if (s.toLowerCase().endsWith(".class")) {
							   items.add(s.substring(Parameters.LANG_FILE_PREFIX.length(), s.length() - 6));
						   } else if (s.endsWith(".po")) {
							   items.add(s.substring(Parameters.LANG_FILE_PREFIX.length(), s.length() - 3));
						   }
					   } else if (s.startsWith(langFilePref) && s.endsWith(".po")) {
						   items.add(s.substring(langFilePref.length(), s.length() - 3));
					   }
				   }
			   }
		   }

		   languagesCombo.addItem(new FlagComboItem(" "));
		   for (String itm : items) {
			  languagesCombo.addItem(new FlagComboItem(itm));
		   }

		   if (lang != null && ! "".equals(lang.toString())) {
			   languagesCombo.setSelectedItem(lang);
		   }
	   }
   }

   private String getLangDir() {

	   return Parameters.formatLangDir(
			   params.getProperty(Parameters.LANG_DIRECTORY));

   }


   private class FlagComboItem {
	   private ImageIcon icon;
	   public final String langCode, longName;

	   public FlagComboItem(String langCode) {
			super();
			String s = "";
			if (langCode != null && langLongName.containsKey(langCode)) {
				s = langLongName.get(langCode);
				if (s != null && ! "".equals(s)) {
					s = " - " + s;
				}
			}
			this.langCode = langCode;
			this.longName = s;

			if (langCode == null || "".equals(langCode.trim())) {
				icon = null;
			} else if ("tst".equals(langCode) || "txt".equals(langCode) || langCode.length() > 3) {
				icon = BLANK_ICON;
			} else {
				icon = Common.readIcon(FLAG_DIR + langCode + ".png");
				if (icon == null) {
					icon = BLANK_ICON;
				}
			}
			langItmHash.put(langCode, this);
	   }

	   public String toString() {
		   return langCode;
	   }
   }


   private static class FlagComboRenderer extends JLabel
   implements ListCellRenderer {


	   private FlagComboRenderer() {
		   setOpaque(true);
		   //setHorizontalAlignment(CENTER);
		   setVerticalAlignment(CENTER);
	   }

	   /*
	    * This method finds the image and text corresponding
	    * to the selected value and returns the label, set up
	    * to display the text and image.
	    */
	   public Component getListCellRendererComponent(
			   JList list,
			   Object value,
			   int index,
			   boolean isSelected,
			   boolean cellHasFocus) {
		   //Get the selected index. (The index param isn't
		   //always valid, so just use the value.)


		   if (value instanceof FlagComboItem) {
			   FlagComboItem ci = (FlagComboItem) value;
			   super.setIcon(ci.icon);
			   super.setText(ci.langCode + ci.longName);
		   } else {
			   super.setIcon(null);
			   super.setText(value.toString());
		   }
		   if (isSelected) {
			   setBackground(list.getSelectionBackground());
			   setForeground(list.getSelectionForeground());
		   } else {
			   setBackground(list.getBackground());
			   setForeground(list.getForeground());
		   }

		   return this;
	   }
   }


}
