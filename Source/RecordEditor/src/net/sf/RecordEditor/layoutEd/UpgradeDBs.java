/*
 * Created on 5/09/2004
 *
 * Changes
 * # Version 0.56 Bruce Martin 2007/01/16
 *   - changed to use ReFrame (from JFrame) which keeps track
 *     of the active form
 *   - Added 0.56 upgrade option (adds new Fujitsu and null
 *     terminated types + new Fujitsu reader/writer)
 *
 * # Version 0.60 Bruce Martin 2007/02/16
 *   - added version 0.60 upgrade option
 */
package net.sf.RecordEditor.layoutEd;


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JEditorPane;

import net.sf.RecordEditor.re.util.UpgradeDB;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.SwingUtils;





/**
 * This will optionally upgrade the RecordEditor Databases to
 * to the latest version
 *
 *
 * @author Bruce Martin
 * @version 0.56
 *
 * Modification log:
 * On 2006/06/28 by Jean-Francois Gagnon:
 *    - Added Additional upgrade from 0.55 to 0.56 to add the
 *      new table entries that relate to the three new data types
 *      and one new Line IO Provider
 */
@SuppressWarnings("serial")
public class UpgradeDBs extends ReFrame implements ActionListener {

	private static final String UPGRADE_DB_MSG = "Upgrade the DB from {0} to version {1}";

	private String formDescription;

		/* screen fields */
	private JEditorPane tips;

	private JButton upgrade55		= new JButton("*");
	//private JButton upgrade56         = new JButton("*");
	//private JButton upgrade60         = new JButton("*");
	private JButton upgrade61b		= new JButton("*");
//	private JButton upgrade67		= new JButton("*");
	private JButton upgrade69		= new JButton("*");
	private JButton upgrade80		= new JButton("*");
	private JButton upgrade90		= new JButton("*");
	private JButton upgrade93		= new JButton("*");
	private JButton upgrade94		= new JButton("*");
	private JButton upgrade95c		= new JButton("*");
	private JButton deleteExamples	= new JButton("*");
	private JButton helpBtn			= SwingUtils.getHelpButton();
	private JCheckBox splitOnRedefine = new JCheckBox();

	private BaseHelpPanel pnl = new BaseHelpPanel();


		/* input params */
	private int connectionId;

	private static final int TIPS_HEIGHT      = SwingUtils.STANDARD_FONT_HEIGHT * 10;
	private static final int FORM_WIDTH       = SwingUtils.STANDARD_FONT_WIDTH * 67;
	private static final int FORM_HEIGHT_INC  = SwingUtils.NORMAL_FIELD_HEIGHT;

	/**
	 * This class Loads selected copybooks into the record editor DB
	 * @param pDBid Database Name
	 * @param pConnectionId Database index (or identifier
	 */
	public UpgradeDBs(final String pDBid,
					  final int pConnectionId)  {
		super(pDBid, "Upgrade", null);

		this.connectionId = pConnectionId;

		formDescription = LangConversion.convertId(LangConversion.ST_MESSAGE, "UpgradeDbHint",
				"The options available on this screen are<ol compact>"
				+ "<li><font COLOR=Blue>Upgrade the DB to "
		    	+ "<b> the latest version of the Databases</b></font>"
				+ " <p>This option should be used <b>only once</b>"
				+ " when using upgrade package"
				+ "<li>Update the Record Seperator to <font COLOR=Blue>"
				+ "default</font>. Again this should only be done once.</ol>");
		tips = new JEditorPane("text/html", formDescription);
		tips.setEditable(false);

		splitOnRedefine.setSelected(false);

		//tips.setCaretPosition(1);

		pnl.setHelpURLre(Common.formatHelpURL(Common.HELP_UPGRADE));

		pnl.addLineRE("", null, helpBtn);
		pnl.setGapRE(BasePanel.GAP1);

		pnl.addComponentRE(1, 5, TIPS_HEIGHT, BasePanel.GAP3,
		        BasePanel.FULL, BasePanel.FULL,
				tips);
		pnl.setGapRE(BasePanel.GAP2);

		//pnl.addMenuItem("Upgrade from 0.52.1/0.53 to version 0.55", upgrade55);
		//pnl.addMenuItem("Upgrade the Tables from 0.55 to 0.56", upgrade56);
		//pnl.addMenuItem("Upgrade the Tables from 0.56 to 0.60", upgrade60);


		pnl.addMenuItemNativeRE(
				LangConversion.convertId(
						LangConversion.ST_FIELD, "",
						UPGRADE_DB_MSG,
						new Object[] {"0.55 - 0.61b", "62"}),
				upgrade61b);
		//pnl.addMenuItem("Upgrade the Tables from 0.62 to version 0.67", upgrade67);
		pnl.addMenuItemNativeRE(
				LangConversion.convertId(
						LangConversion.ST_FIELD, "",
						UPGRADE_DB_MSG,
						new Object[] {"0.62->69*", "0.69.2c"}),
				upgrade69);
		pnl.addMenuItemNativeRE(
				LangConversion.convertId(
						LangConversion.ST_FIELD, "",
						UPGRADE_DB_MSG,
						new Object[] {"0.69*", "0.80"}),
				upgrade80);

		pnl.addMenuItemNativeRE(
				LangConversion.convertId(
						LangConversion.ST_FIELD, "",
						UPGRADE_DB_MSG,
						new Object[] {"0.80*", "0.93"}),
				upgrade90);
		pnl.addMenuItemNativeRE(
				LangConversion.convertId(
						LangConversion.ST_FIELD, "",
						UPGRADE_DB_MSG,
						new Object[] {"0.90", "0.93"}),
				upgrade93);
		pnl.addMenuItemNativeRE(
				LangConversion.convertId(
						LangConversion.ST_FIELD, "",
						UPGRADE_DB_MSG,
						new Object[] {"0.93", "0.96h"}),
				upgrade94);
		pnl.addMenuItemNativeRE(
				LangConversion.convertId(
						LangConversion.ST_FIELD, "",
						UPGRADE_DB_MSG,
						new Object[] {"0.94", "0.98"}),
				upgrade95c);
		pnl.setGapRE(BasePanel.GAP1);
		pnl.addMenuItemRE("Delete example Layout's from the DB", deleteExamples);

		helpBtn.addActionListener(this);
		upgrade55.addActionListener(this);
		//upgrade56.addActionListener(this);
		//upgrade60.addActionListener(this);
		upgrade61b.addActionListener(this);
		//upgrade67.addActionListener(this);
		upgrade69.addActionListener(this);
		upgrade80.addActionListener(this);
		upgrade90.addActionListener(this);
		upgrade93.addActionListener(this);
		upgrade94.addActionListener(this);
		upgrade95c.addActionListener(this);
		deleteExamples.addActionListener(this);

		this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);

		//pnl.done();

		this.getContentPane().add(pnl);

		pack();

		setBounds(getY(), getX(), FORM_WIDTH, getHeight() + FORM_HEIGHT_INC);

		show();

	}


	/**
	 * @see java.awt.Event.actionPerformed
	 */
	public void actionPerformed(final ActionEvent event) {
		UpgradeDB upgrade = new UpgradeDB();

	    if (event.getSource() == helpBtn) {
	        pnl.showHelpRE();
	    } else if (event.getSource() == upgrade55) {
	    	upgrade.upgrade55(connectionId);
//	    } else if (event.getSource() == upgrade56) {
//	        UpgradeDB.upgrade56(connectionId);
	    //} else if (event.getSource() == upgrade60) {
	    //    UpgradeDB.upgrade60(connectionId);
	    } else if (event.getSource() == upgrade61b) {
	    	upgrade.upgrade61b(connectionId);
	    //} else if (event.getSource() == upgrade67) {
	    //	upgrade.upgrade67(connectionId);
	    } else if (event.getSource() == upgrade69) {
	    	upgrade.upgrade69(connectionId);
	    } else if (event.getSource() == upgrade80) {
	    	upgrade.upgrade71(connectionId);
	    } else if (event.getSource() == upgrade90) {
	    	upgrade.upgrade90(connectionId);
	    } else if (event.getSource() == upgrade93) {
	    	upgrade.upgrade93(connectionId);
	    } else if (event.getSource() == upgrade94) {
	    	upgrade.upgrade94(connectionId);
	    } else if (event.getSource() == upgrade95c) {
	    	upgrade.upgrade96(connectionId);
	    } else if (event.getSource() == deleteExamples) {
	    	upgrade.deleteExamples(connectionId);
	    } else {
	    	upgrade.updateRecordSepList(connectionId);
	    }
	    upgrade.loadHeldLayouts();
	}
}
