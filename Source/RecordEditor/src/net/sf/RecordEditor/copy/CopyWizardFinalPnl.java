/**
 * 
 */
package net.sf.RecordEditor.copy;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

import net.sf.RecordEditor.jibx.JibxCall;
import net.sf.RecordEditor.jibx.compare.CopyDefinition;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.Parameters;
import net.sf.RecordEditor.utils.openFile.AbstractLayoutSelection;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.FileChooser;
import net.sf.RecordEditor.utils.wizards.AbstractWizardPanel;

/**
 * @author Bruce Martin
 *
 */
public class CopyWizardFinalPnl extends BaseHelpPanel implements AbstractWizardPanel<CopyDefinition> {

	private FileChooser saveFileName = new FileChooser();
	
	private AbstractLayoutSelection<?> selection;
	private AbstractLayoutSelection<?> selection2;
	
	private JButton saveBtn = new JButton("Save", Common.getRecordIcon(Common.ID_SAVE_ICON)); 
	private JButton runBtn  = new JButton("Copy");
//	private JButton htmlBtn = new JButton("Compare (HTML)");
	
	private JRadioButton stripTrailingSpaces = new JRadioButton("Strip Trailing Spaces");

	private JTextField message        = new JTextField();
	
	
	private CopyDefinition copyDetail;
	
	private JibxCall<CopyDefinition> jibx = null;
	
	private boolean toRun = true;
	


	
	private AbstractAction btnAction = new AbstractAction() {
		@Override
		public void actionPerformed(ActionEvent e) {

			if (e.getSource() == runBtn) {
				run();
			} else {
				save();
			}
		}
		
	};
	
	
	/**
	 * Final wizard Screen
	 */
	public CopyWizardFinalPnl(
			AbstractLayoutSelection<?> layoutSelection, 
			AbstractLayoutSelection<?> layoutSelection2) {
		super();
		JPanel pnl = new JPanel(new GridLayout(3,2));
		//JPanel pnlStrip = new JPanel();
		
		
		selection = layoutSelection ;
		selection2 = layoutSelection2;
		
		saveFileName.setDefaultDirectory(Parameters.getFileName(Parameters.COMPARE_SAVE_DIRECTORY));

		saveBtn.addActionListener(btnAction);
		runBtn.addActionListener(btnAction);
	
		super.setHelpURL(Common.formatHelpURL(Common.HELP_DIFF_SL));
		
		super.addComponent("Save File", saveFileName, saveFileName.getChooseFileButton());
		super.setGap(BasePanel.GAP1);
		super.addComponent("", stripTrailingSpaces);
		
		super.addComponent("", pnl);
		super.setHeight(BasePanel.GAP5);
		
		super.addComponent("", null, saveBtn);
		super.setGap(BasePanel.GAP0);
		super.addComponent("", null, runBtn);
		super.setGap(BasePanel.GAP2);
		super.addMessage(message);
	}
	

	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#getComponent()
	 */
	@Override
	public final JComponent getComponent() {
		return this;
	}

	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#getValues()
	 */
	@Override
	public final CopyDefinition getValues() throws Exception {
		
		if (! "".equals(saveFileName.getText())) {
			copyDetail.saveFile = saveFileName.getText();
		}
		
		copyDetail.stripTrailingSpaces = stripTrailingSpaces.isSelected();
		//System.out.println("Final Get -Layout Name: " + diffDetail.getLayoutDetails().name);

		return copyDetail;
	}

	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#isMore()
	 */
	@Override
	public final boolean skip() {
		return false;
	}



	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#setValues(java.lang.Object)
	 */
	@Override
	public final void setValues(CopyDefinition detail) throws Exception {
		
		saveFileName.setText(detail.saveFile);
		copyDetail = detail;
		copyDetail.fileSaved = false;
		copyDetail.complete = "YES";
		
		stripTrailingSpaces.setSelected(copyDetail.stripTrailingSpaces);
	}
	
	public final void run() {
		
		try {
			copyDetail = getValues();

			boolean ok = DoCopy.copy(selection, selection2, copyDetail);

			toRun = false;
			if (ok) {
				message.setText("Copy Done !!! ");
			} else {
				message.setText("Copy Done !!!, check log for errors ");
			}
		} catch (Exception e) {
			e.printStackTrace();
			Common.logMsg("Copy Failed", e);
			message.setText("Copy Failed: " + e.getMessage());
		}
	}


	
	/**
	 * Save the file
	 */
	public final void save() {
		try {
			copyDetail = getValues();
			
		    if (jibx == null) {
			   jibx = new JibxCall<CopyDefinition>(CopyDefinition.class);
		    }
		    jibx.unmarshal(copyDetail.saveFile, copyDetail);
			copyDetail.fileSaved = true;
		} catch (Exception e) {
 		   e.printStackTrace();
		   Common.logMsg("File Save Failed:", e);
		}
	}

	/**
	 * @return the toRun
	 */
	public final boolean isToRun() {
		return toRun;
	}
}
