/*
 * @Author Bruce Martin
 * Created on 30/12/2008
 *
 * Purpose:
 * This class implements a wizard for building Record Layouts
 * from a file
 *
 * Changes
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Changed to use new externalRecord/External field structure
 *   - JRecord related
 *
 * # Version 0.61 Bruce Martin 2007/05/5
 *   - Changes for marathon testing
 *   - Extra error reportin
 */
package net.sf.RecordEditor.utils.wizards;

import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyVetoException;
import java.sql.SQLException;


import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JInternalFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.RootPaneContainer;

import net.sf.JRecord.Log.AbsSSLogger;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReActionHandler;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.screenManager.ReMainFrame;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.BasePanel;



/**
 * This class implements a wizard for building Record Layouts
 * from a file
 *
 * This is an attempt to avoid using Tab pane
 * @author Bruce Martin
 *
 */
public abstract class Z_AbstractWizard_New<Details> /*extends ReFrame*/ implements ActionListener {

    public static final int FORWARD  = 1;
    public static final int BACKWARD = -1;
    private static final int WIDTH_INCREASE = 150;
    private static final int HEIGHT_INCREASE = 75;


    private AbstractWizardPanel<Details>[] pnls;
    private Details wizardDetails;

	private JPanel tabbed = new JPanel();
	//private JPanel tabbed = new JPanel();
	private JTextArea message = new JTextArea();

	private JButton  leftArrow;
	private JButton rightArrow;

	private int panelNumber = 0;

	private boolean toInit = true;
	private Component displayFrame;
	private RootPaneContainer controlFrame;


	private JScrollPane oldPane = null;



	/**
	 * create wizard from name / details
	 *
	 * @param name name of the wizard
	 * @param details wizard details
	 */
	public Z_AbstractWizard_New(String name, final Details details) {
		this(new ReFrame(name,"", null), details);
	}

	/**
	 * File Layout creation wizard
	 * @param frame frame to display details on
	 * @param details wizard details
	 */
	public <T extends Component & RootPaneContainer> Z_AbstractWizard_New(T frame, final Details details) {
		displayFrame = frame;
		controlFrame = frame;
		wizardDetails = details;
	}

//	/**
//     * File Layout creation wizard
//     * @param connectionId Database connection Identifier
//     * @param fileName Name of the file
//     * @param callback callback class (optional) but will be
//     *        called when a layout has been created
//     */
//    public AbstractWizard(JInternalFrame frame, final Details details,
//            final AbstractWizardPanel<Details>[] panels) {
//    	this(frame, details);
//
//    	setPanels(panels);
//    }

    /**
     * Set the panels
     * @param panels the panels up
     */
    public void setPanels(final AbstractWizardPanel<Details>[] panels) {
    	setPanels(panels, true);
    }

    public void setPanels(final AbstractWizardPanel<Details>[] panels, boolean visible) {
    	int height = 0;
    	int width = 0;
    	Dimension d;
        pnls = panels;

        for (int i = 0; i < pnls.length; i++) {
        	pnls[i].getComponent().setBorder(BorderFactory.createEmptyBorder());
        }
        if (toInit) {
        	//JPanel pnl = new JPanel();
        	//JScrollPane scrollTabbed=  new JScrollPane(tabbed);
        	//scrollTabbed.setBorder(BorderFactory.createEmptyBorder());
        	BaseHelpPanel pnl = new BaseHelpPanel();

        	pnl.addComponent(1, 5, BasePanel.FILL, BasePanel.GAP,
                    BasePanel.FULL, BasePanel.FULL,
                    tabbed);
        	pnl.addComponent(1, 5, BasePanel.PREFERRED, BasePanel.GAP,
                    BasePanel.FULL, BasePanel.FULL,
                    getBottomSection());

        	toInit = false;

  	        //pnl.setLayout(new BorderLayout());
	        //pnl.add(BorderLayout.CENTER, holderPnl);
	        //pnl.add(BorderLayout.SOUTH, getBottomSection());
	        //addPanel(0);
	        controlFrame.getContentPane().add(pnl);

	        int pnlHeight=0,
	            pnlWidth=0;
	        width = 0;
	        height = 0;

	        for (int i = 0; i < pnls.length; i++) {
	            tabbed.add(pnls[i].getComponent());
	            pnls[i].getComponent().setLayout(new BorderLayout());
	            displayFrame.doLayout();

		        d = displayFrame.getPreferredSize();
		       // pnls[i].getComponent().getPreferredSize();
		        width = Math.max(width, d.width);
		        height = Math.max(height, d.height);
		        d = pnls[i].getComponent().getSize();
		        pnlWidth = Math.max(pnlWidth, d.width);
		        pnlHeight = Math.max(pnlHeight, d.height);

		        tabbed.remove(pnls[i].getComponent());
	        }

	        d = new Dimension(pnlWidth, pnlHeight);
	        System.out.println(" -->  " + pnlWidth + " " + pnlHeight);
//	        for (int i = 0; i < pnls.length; i++) {
//	            pnls[i].getComponent().setPreferredSize(d);
//	        }




	        d = displayFrame.getPreferredSize();
	        width += WIDTH_INCREASE;
	        height += HEIGHT_INCREASE;
	        ReMainFrame frame = ReMainFrame.getMasterFrame();
	        if (frame != null) {
	        	height = Math.min(height+3, frame.getDesktop().getHeight() - 1);
	        	width  = Math.min(width, frame.getDesktop().getWidth() - 1);
	        }
	        displayFrame.setBounds(displayFrame.getY(), displayFrame.getX(), width, height);

	        try {
	            pnls[0].setValues(wizardDetails);
	        } catch (Exception ex) { ex.printStackTrace(); }

	        addPanel(0);
        }

        if (visible) {
        	displayFrame.setVisible(true);
        }
    }

    /**
     * Build the bottom section (arrows + message Field)
     *
     * @return the bottom section
     */
    private JPanel getBottomSection() {
        JPanel ret = new JPanel();
        ImageIcon[]   icon = Common.getArrowIcons();

        leftArrow = new JButton("", icon[1]);
        rightArrow = new JButton("", icon[2]);

        leftArrow.addActionListener(this);
        rightArrow.addActionListener(this);

        ret.setLayout(new BorderLayout());
        ret.add(BorderLayout.WEST, leftArrow);
        ret.add(BorderLayout.SOUTH, new JScrollPane(message));
        ret.add(BorderLayout.EAST, rightArrow);
         return ret;
    }



    /**
     * @see java.awt.event.ActionListener#actionPerformed(java.awt.event.ActionEvent)
     */
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == leftArrow) {
            if (panelNumber > 0) {
                changePanel(BACKWARD);
            }
        } else if (e.getSource() == rightArrow) {
            if ((panelNumber < pnls.length - 1)) {
                changePanel(FORWARD);
            } else {
            	ap_200_finish();
            }
        }
    }

    /**
     * Change the panel
     * @param inc direction of change (forward (+1) or backward (-1))
     */
    public void changePanel(int inc) {

        int old = panelNumber;
        try {
        	wizardDetails = pnls[panelNumber].getValues();

            panelNumber += inc;
        	do {
	            pnls[panelNumber].setValues(wizardDetails);
        	} while (pnls[panelNumber].skip() && (panelNumber > 0) && ((panelNumber += inc) < pnls.length)  );

//        	System.out.println("~~> Next Panel " + panelNumber + " < " + pnls.length);
        	if (panelNumber < pnls.length) {
        		//tabbed.addTab("", pnls[panelNumber].getComponent());
            	//tabbed.remove(pnls[old].getComponent());
        		addPanel(panelNumber);
        	} else {
        		panelNumber = old;
        		ap_200_finish();
        	}
        } catch (Exception ex) {
            panelNumber = old;
            message.setText(ex.getMessage());
            Common.logMsg(AbsSSLogger.WARNING, ex.getMessage(), null);
            ex.printStackTrace();
        }
    }

    private void addPanel(int num) {

    	JScrollPane tmp = new JScrollPane(pnls[panelNumber].getComponent());

		//tabbed.addTab(null, tmp);

		if (oldPane != null) {
			tabbed.remove(oldPane);
		}
		tabbed.add(tmp);

		tabbed.invalidate();
		//tabbed.revalidate();
		//tabbed.doLayout();
		//tabbed.repaint();
		//displayFrame.doLayout();
		//displayFrame.repaint();
		//controlFrame.p

		//controlFrame.getContentPane().invalidate();
		controlFrame.getContentPane().revalidate();
		displayFrame.doLayout();
		displayFrame.repaint();


		oldPane = tmp;

    }

    private void ap_200_finish() {

        try {
        	wizardDetails = pnls[panelNumber].getValues();
        	finished(wizardDetails);
        } catch (Exception ex) {
            message.setText(ex.getMessage());
            Common.logMsgRaw(ex.getMessage(), ex);
            ex.printStackTrace();
        }
    }


    /**
     * save the newly created record to the DB
     * @throws SQLException any error that occured
     */
    public abstract void finished(Details details);




    /**
     * @see net.sf.RecordEditor.utils.common.ReActionHandler#executeAction(int)
     */
    public void executeAction(int action) {

        if (action == ReActionHandler.HELP) {
            pnls[panelNumber].showHelp();
        } else if (displayFrame instanceof ReFrame) {
        	((ReFrame) displayFrame).executeAction(action);
        }
    }

    /**
     * @see net.sf.RecordEditor.utils.common.ReActionHandler#isActionAvailable(int)
     */
    public boolean isActionAvailable(int action) {

        return action == ReActionHandler.HELP
            || ((		displayFrame instanceof ReFrame
            	&& ((ReFrame) displayFrame).isActionAvailable(action)));
    }

	/**
	 * @return the wizardDetails
	 */
    public Details getWizardDetails() {
    	try {
    		wizardDetails = pnls[panelNumber].getValues();
    	} catch (Exception e) {
		}
		return wizardDetails;
	}

	/**
	 * @param wizardDetails the wizardDetails to set
	 */
    public void setWizardDetails(Details wizardDetails) {
		this.wizardDetails = wizardDetails;
	}


	/**
	 * @return the panelNumber
	 */
	public final AbstractWizardPanel<Details> getActivePanel() {
		return pnls[panelNumber];
	}

	/**
	 * @return the message
	 */
	public final JTextArea getMessage() {
		return message;
	}

	/**
	 * @return the panelNumber
	 */
	public final int getPanelNumber() {
		return panelNumber;
	}

	/**
	 * Close the frame
	 */
	public final void setClosed(boolean close)
	throws PropertyVetoException {

//		System.out.println("setClosed: " + displayFrame.getClass().getName()
//				+ " --> " + (displayFrame instanceof JInternalFrame));
		if (displayFrame instanceof JInternalFrame) {
			((JInternalFrame) displayFrame).setClosed(close);
		} else {
			displayFrame.setVisible(! close);
		}
	}



//    /**
//     *  test the wizard
//     * @param args program arguments
//     */
//    public static void main(String[] args) {
//
//        System.out.println();
//        (new ReMainFrame("Wizard Test", "")).buildMenubar();;
//        new Wizard(0, "C:\\Documents and Settings\\b\\My Documents\\Ams_LocDownload_20041228.txt", null);
//    }
  }
