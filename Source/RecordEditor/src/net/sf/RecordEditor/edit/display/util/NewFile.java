package net.sf.RecordEditor.edit.display.util;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JInternalFrame;
import javax.swing.JTabbedPane;

import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.RecordEditor.edit.util.NewCsvFile;
import net.sf.RecordEditor.re.display.DisplayBuilderFactory;
import net.sf.RecordEditor.re.openFile.AbstractLayoutSelection;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.SwingUtils;

public class NewFile {

	private final ReFrame frame = new ReFrame("","New Csv File", null);
	private JTabbedPane tab = new JTabbedPane();
	private JButton    goBtn	     = SwingUtils.newButton("Create");
	//private JTextField msgTxt	     = new JTextField();
	private AbstractLayoutSelection layoutSelect;

	BaseHelpPanel panel = new BaseHelpPanel();


	public NewFile(AbstractLayoutSelection layoutSelection) {

		layoutSelect = layoutSelection;

		init_100_Setup();
		init_200_LayoutScreen();
		init_300_Listners();

		frame.setVisible(true);
		frame.setToMaximum(false);
	}

	private void init_100_Setup() {


	}

	private void init_200_LayoutScreen() {
		BasePanel pnl = new BasePanel();

		NewCsvFile csvFile = new NewCsvFile(frame);

		panel.setGapRE(BasePanel.GAP2);

		layoutSelect.addLayoutSelection(panel, null, null, null, null);

		panel.setGapRE(BasePanel.GAP1);
		panel.addLineRE(null, null, goBtn);
		panel.setGapRE(BasePanel.GAP4);
		panel.addMessageRE();
		panel.setHeightRE(BasePanel.HEIGHT_1P6);

		SwingUtils.addTab(tab, "NewFileTab", "Normal File", panel);
		SwingUtils.addTab(tab, "NewFileTab", "Csv File", csvFile.panel);

		pnl.setGapRE(2);
		pnl.addComponentRE(0, 6, BasePanel.FILL,
		        2,
		        BasePanel.FULL, BasePanel.FULL,
		        tab);

		frame.addMainComponent(pnl);
		frame.setSize(
				Math.min(frame.getWidth() + 80,
						 ReFrame.getDesktopWidth() - 2),
				Math.min(frame.getHeight(),
						 ReFrame.getDesktopHeight() - 2));

		frame.setDefaultCloseOperation(JInternalFrame.DISPOSE_ON_CLOSE);
	}



	private void init_300_Listners() {
		goBtn.addActionListener(new ActionListener() {

			/* (non-Javadoc)
			 * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
			 */
			@Override
			public void actionPerformed(ActionEvent e) {
				try {
					AbstractLayoutDetails layout = layoutSelect.getRecordLayout("");

					if (layout == null) {
						panel.setMessageTxtRE("Error Retrieving Layout");
					} else {
						DisplayBuilderFactory.startEditorNewFile(layout);
//						FileView file = new FileView(
//								DataStoreStd.newStore(layout),
//								null,
//								null,
//								false);
//						DisplayBuilderFactory.getInstance().newDisplay(DisplayBuilderFactory.ST_INITIAL_EDIT, "", null, file.getLayout(), file, 0);
						//DisplayBuilder.doOpen(file, 0, false);

						frame.setVisible(false);
						frame.doDefaultCloseAction();
					}
				} catch (Exception ex) {
					panel.setMessageTxtRE("Error Creating File: ", ex.getMessage());
				}
			}
		});
	}

}
