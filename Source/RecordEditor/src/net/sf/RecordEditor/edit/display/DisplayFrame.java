package net.sf.RecordEditor.edit.display;


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.JComponent;
import javax.swing.JOptionPane;
import javax.swing.JSplitPane;
import javax.swing.JTabbedPane;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.InternalFrameAdapter;
import javax.swing.event.InternalFrameEvent;

import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.RecordEditor.edit.display.common.ILayoutChanged;
import net.sf.RecordEditor.edit.util.ReMessages;
import net.sf.RecordEditor.re.display.AbstractFileDisplay;
import net.sf.RecordEditor.re.display.DisplayDetails;
import net.sf.RecordEditor.re.display.IDisplayFrame;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReActionHandler;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.screenManager.ReMainFrame;
import net.sf.RecordEditor.utils.swing.SwingUtils;
import net.sf.RecordEditor.utils.swing.TabWithClosePnl;


@SuppressWarnings("serial")
public class DisplayFrame extends ReFrame implements IDisplayFrame<BaseDisplay>, ILayoutChanged {


//    private final ArrayList<AbstractFileDisplay> childScreens = new ArrayList<AbstractFileDisplay>();
    private ArrayList<BaseDisplay> mainScreens = new ArrayList<BaseDisplay>();
    private ArrayList<JSplitPane> splitPanes = new ArrayList<JSplitPane>();
    private JTabbedPane pane = null;


    private ChangeListener tabListner = new ChangeListener() {

        @Override
        public void stateChanged(ChangeEvent e) {

            ReMainFrame.getMasterFrame().focusChanged(DisplayFrame.this);
        }
    };

    InternalFrameAdapter closingAction = new InternalFrameAdapter() {

            public void internalFrameClosing(InternalFrameEvent e)  {
                 windowClosingCheck();
            }
        };


    public DisplayFrame(BaseDisplay d) {
    	super(d.getFileView().getBaseFile().getFileNameNoDirectory(), d.formType, d.getFileView().getBaseFile());

        this.setPrimaryView(d.primary);
        add(d);

        d.setParentFrame(this, true);

        this.setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);

        this.addInternalFrameListener(closingAction);

    }



    /* (non-Javadoc)
	 * @see net.sf.RecordEditor.re.script.IDisplayFrame#getReFrame()
	 */
	@Override
	public ReFrame getReFrame() {
		return this;
	}



	/* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#addScreen(net.sf.RecordEditor.edit.display.BaseDisplay)
     */
    @Override
    public final void addScreen(BaseDisplay d) {
        addScreen(d,  true);
    }

    public final void addScreen(BaseDisplay d, boolean rebuild) {
        add(d);

        d.setParentFrame(this, false);
        d.getActualPnl().done();

        if (rebuild) {
            bldScreen();
        }
        if (pane != null) {
            pane.setSelectedIndex(pane.getTabCount() - 1);
        }
    }

    private void add(BaseDisplay d) {

    	if (d.getDockingPopup() == null) {
    		d.setDockingPopup(new net.sf.RecordEditor.edit.display.util.DockingPopupListner(d));
    	}
        mainScreens.add(d);
        //childScreens.add(c);
        splitPanes.add(null);
    }

    /**
     *
     * Check if changes to be saved
     */
    public void windowClosingCheck() {
        boolean doClose = true;

       	this.removeInternalFrameListener(closingAction);

        if (mainScreens.size() > 0) {
            BaseDisplay main = mainScreens.get(0);
            FileView fileView = main.getFileView();
            if (super.isPrimaryView()) {
                ReFrame[] allFrames = ReFrame.getAllFrames();
                FileView fileMaster = fileView.getBaseFile();
                //System.out.println("closeWindow " + this.getName());

                for (int i = allFrames.length - 1; i >= 0; i--) {
                    if (allFrames[i].getDocument() == fileMaster
                            && (allFrames[i] != this)) {
                        allFrames[i].reClose();
                    }
                }

                if (fileMaster != null && fileMaster.isChanged() && fileMaster.isSaveAvailable()
                && ! ReFrame.isForcedClose()) {
                    int result = JOptionPane.showConfirmDialog(
                            null,
                            ReMessages.SAVE_CHANGES.get(),
                            //LangConversion.convert(LangConversion.ST_MESSAGE, "Save changes"),
                            ReMessages.SAVE_CHANGES_FILE.get(fileMaster.getFileName()),
                            //LangConversion.convert("Save Changes to file: {0}", fileMaster.getFileName()),
                            JOptionPane.YES_NO_OPTION);

                    if (result == JOptionPane.YES_OPTION) {
                        doClose = main.saveFile();
                    }
                }


                if (doClose) {
	                if (fileView != null && fileMaster.isSaveAvailable()) {
	                    fileView.clear();
	                }
                }
            }

            if (doClose) {
            	ArrayList<FileView> views = new ArrayList<FileView>();
             	for (int i = mainScreens.size() - 1; i > 0; i-- ) {
             		views.add(mainScreens.get(i).getFileView());
             		mainScreens.get(i).closeWindow();
             	}
             	
                main.doClose();
                
                mainScreens.clear();
             	for (FileView f : views) {
             		checkTheViewIsUsed(f);
             	}
                super.dispose();
            }
        } else {
            super.dispose();
        }
        //super.windowClosing();
    }


    /* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#close(net.sf.RecordEditor.edit.display.BaseDisplay)
     */
    @Override
    public final void close(AbstractFileDisplay d) {

        for (int i = 0; i < mainScreens.size(); i++) {
            if (mainScreens.get(i) == d) {
                close(i);
                break;
            }
        }

        if ( mainScreens.size() == 0) {
        	super.dispose();
        }
    }

    public final void close(int idx) {

    	FileView fileView = mainScreens.get(idx).getFileView();

        mainScreens.get(idx).doClose();
        removeIdx(idx);
        
//      if (mainScreens.size() == 0) {
//      reClose();
//  }
        
        checkTheViewIsUsed(fileView);
        
    }
    
    private void checkTheViewIsUsed(FileView fileView) {
    	if (fileView == null) return;
        ReFrame[] frames = ReFrame.getAllFrames();
        boolean notUsed = true;

        for (int i = 0; i < frames.length && notUsed; i++) {
			if (frames[i] instanceof DisplayFrame 
			&&  frames[i].getDocument() != null
			&& ((DisplayFrame) frames[i]).getDocument() == fileView.getBaseFile()) {
				ArrayList<BaseDisplay> ms = ((DisplayFrame) frames[i]).mainScreens;
				for (BaseDisplay baseDisplay : ms) {
					if (baseDisplay.getFileView() == fileView) {
						notUsed = false;
						break;
					}
					
				}
			} else {
				AbstractFileDisplay displayDetails = DisplayDetails.getDisplayDetails(frames[i]);
				notUsed = displayDetails == null || displayDetails.getFileView() != fileView;
			}
		}
        
        if (notUsed) {
        	fileView.clear();
        }
    }

    private void moveToSeperateScreen() {
        if (pane != null) {
            DisplayFrame disp = this;
            DisplayFrame p;
            int displIdx = getActiveIdx();

            for (int i = mainScreens.size() - 1; i > 0; i--) {
                p = moveToSeperateScreenI(i);
                if (i == displIdx && p != null) {
                    disp = p;
                }
            }

            disp.moveToFront();
        }
    }

    /**
     * Un-Dock a panel
     * @param pnl panel to un-dock
     */
    @Override
    public void moveToSeperateScreen(AbstractFileDisplay pnl) {
        int idx = mainScreens.indexOf(pnl);

        if (idx > 0) {
            moveToSeperateScreen(idx);
        }
    }

    private void moveToSeperateScreen(int idx) {

        DisplayFrame newScreen = moveToSeperateScreenI(idx);

        if (newScreen != null) {
            this.revalidate();

            try {
                newScreen.mainScreens.get(0).setScreenSize(true);
                ReFrame.setActiveFrame(newScreen);
            } catch (Exception e) {

            }
        }
    }

    private DisplayFrame moveToSeperateScreenI(int idx) {
        if (pane != null && idx > 0) {
        	BaseDisplay d = mainScreens.get(idx);
            removeIdx(idx);

            DisplayFrame ret = new DisplayFrame(d);

            d.setScreenSize(true);

            return ret;
        }
        return null;
    }


    private void removeIdx(int idx) {

        mainScreens.remove(idx);
        //childScreens.remove(idx);
        splitPanes.remove(idx);
        if (pane != null) {
            pane.remove(idx);
            if (pane.getTabCount() == 1) {
                bldScreen();

                mainScreens.get(0).setParentFrame(this, true);
            }
        }
    }

    /* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#reClose()
     */
    @Override
    public final void reClose() {

        BaseDisplay main = null;
        if (mainScreens.size() > 0) {
            main = mainScreens.get(0);
        }

//        for (AbstractFileDisplay d : childScreens) {
//            if (d != null) {
//                d.doClose();
//            }
//        }
        for (AbstractFileDisplay d : mainScreens) {
            d.doClose();
        }

        if (main != null) {
            FileView fileView = main.getFileView();
            if (super.isPrimaryView()) {
                if (fileView != null) {
                    main.closeWindow();

                    if (fileView == fileView.getBaseFile() && super.isPrimaryView()) {
                        fileView.clear();
                    }
                }
             }
            
            checkTheViewIsUsed(fileView);
        }
        super.reClose();
    }


    /**
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#setToActiveTab()
     */
    @Override
    public final void setToActiveTab(AbstractFileDisplay pnl) {
        int idx = mainScreens.indexOf(pnl);
        if (idx >= 0 && pane != null && pane.getSelectedIndex() != idx) {
            pane.setSelectedIndex(idx);
        }
    }

    /**
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#setToActiveFrame()
     */
    @Override
    public final void setToActiveFrame() {
        super.setActiveFrame(this);
    }


    @Override
    public void setToMaximum(boolean max) {
        boolean recalc = super.isMaximum() != max;

        super.setToMaximum(max);

        if (recalc) {
            recalcSplits();
        }
    }

    private void recalcSplits() {

        //boolean update = false;
        for (int i = 0; i < mainScreens.size(); i++) {
            if (splitPanes.get(i) != null && mainScreens.get(i).getChildScreen() != null) {
                splitPanes.get(i).setDividerLocation(this.calcSplit(i));
            }
        }

    }

    /* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#bldScreen()
     */
    @Override
    public final void bldScreen() {

        if (mainScreens.size() == 1) {
            this.getContentPane().removeAll();

            addMainComponent(getScreen(0));

            if (pane != null) {
                pane.removeChangeListener(tabListner);
                pane = null;
            }
        } else {
            if (pane == null || Common.TEST_MODE) {
                this.getContentPane().removeAll();
                pane = new JTabbedPane();
//				pane.putClientProperty(SubstanceLookAndFeel.TABBED_PANE_CLOSE_BUTTONS_PROPERTY,
//						Boolean.TRUE);

                addTabs();

                pane.addChangeListener(tabListner);

                this.getContentPane().add(pane);
            } else {
                pane.removeAll();

                addTabs();
            }
        }
//		if (mainScreens.size() > 0) {
//			mainScreens.get(0).setParentFrame(this, true);
//		}
        this.revalidate();
    }

    private void addTabs() {
        for (int i = 0; i < mainScreens.size(); i++) {
            pane.addTab(mainScreens.get(i).formType, getScreen(i));
        }
        for (int i = 0; i < mainScreens.size(); i++) {
            pane.setTabComponentAt(i, new TabButton(mainScreens.get(i), i > 0));
        }
    }

    private JComponent getScreen(int idx) {
        if (mainScreens.get(idx).getChildScreen() == null) {
            return mainScreens.get(idx).getActualPnl();
        }

        int splitType = JSplitPane.HORIZONTAL_SPLIT;
        if (mainScreens.get(idx).getCurrentChildScreenPostion() == AbstractCreateChildScreen.CS_BOTTOM) {
        	splitType =  JSplitPane.VERTICAL_SPLIT;
        }

        JSplitPane sp = new JSplitPane(
        		splitType,
                mainScreens.get(idx).getActualPnl(),
                mainScreens.get(idx).getChildScreen().getActualPnl());


        splitPanes.set(idx, sp);

        sp.setDividerLocation(calcSplit(idx));
        return sp;
//			System.out.println("~~ " +  this.getWidth() + " - " + childScreens.get(idx).getActualPnl().getPreferredSize().width
//					+ " - " + (SwingUtils.CHAR_WIDTH * 3)
//					+ " , " + mainScreens.get(idx).actualPnl.getPreferredSize().width);
//
//			System.out.println("~~ Split Divder pre  ~~>> " +  sp.getDividerLocation() + " " + w1
//					+ " $$ " + w0 + " " + childScreens.get(idx).getActualPnl().getPreferredSize().width);
//			//sp.setDividerLocation(w1);
//			System.out.println("~~ Split Divder post ~~>> " +  sp.getDividerLocation());
//
//			System.out.println("~~ Split ~~>> "  + mainScreens.get(idx).actualPnl.getPreferredSize().width
//					+ " ! " + childScreens.get(idx).getActualPnl().getPreferredSize().width
//					+ " >> " + w1 + " " + this.getWidth());
//			System.out.println("~~ Split ~~>> "  + mainScreens.get(idx).actualPnl.getMaximumSize().width
//					+ " ! " + childScreens.get(idx).getActualPnl().getMaximumSize().width
//					+ " >> Maximum");
//			System.out.println("~~ Split ~~>> "  + mainScreens.get(idx).actualPnl.getMinimumSize().width
//					+ " ! " + childScreens.get(idx).getActualPnl().getMinimumSize().width
//					+ " >> Minimum ");


    }

    private int calcSplit(int idx) {
    	if (mainScreens.get(idx).getCurrentChildScreenPostion() == AbstractCreateChildScreen.CS_BOTTOM) {
    		return Math.max(this.getHeight() - mainScreens.get(idx).getChildScreen().getActualPnl().getPreferredSize().height
                    - (SwingUtils.CHAR_FIELD_HEIGHT * 3),
                    mainScreens.get(idx).getActualPnl().getPreferredSize().height);
    	}
//    	System.out.println("calc split: \n"
//    			 + this.getWidth() + " - " + mainScreens.get(idx).getChildScreen().getActualPnl().getPreferredSize().width
//    			 + " - " + (SwingUtils.CHAR_FIELD_WIDTH * 3) +"\n "
//    			 + mainScreens.get(idx).actualPnl.getPreferredSize().width);
        return Math.max(
                this.getWidth() - mainScreens.get(idx).getChildScreen().getActualPnl().getPreferredSize().width
                - SwingUtils.CHAR_FIELD_WIDTH * 3,
                mainScreens.get(idx).getActualPnl().getPreferredSize().width - SwingUtils.CHAR_FIELD_WIDTH * 30);
    }

    /* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#getActiveDisplay()
     */
    @Override
    public BaseDisplay getActiveDisplay() {
        if (mainScreens.size() == 0) return null;
        return mainScreens.get(getActiveIdx());
    }


	private int getActiveIdx() {
        if (pane == null) {
            return 0;
        }

        return Math.max(0, pane.getSelectedIndex());
    }

    public final void setActiveIdx(int newIdx) {
        if (pane == null || newIdx < 0 || newIdx >= pane.getTabCount()) {
            return;
        }

        pane.setSelectedIndex(newIdx);
    }

    /**
     * The number of active screens
     * @return number of active screens
     */
    @Override
    public int getScreenCount() {
        return mainScreens.size();
    }

    /**
     * Get the index of a panel
     * @param pnl panel to search for
     * @return index of a panel
     */
    @Override
    public int indexOf(AbstractFileDisplay pnl) {
        return mainScreens.indexOf(pnl);
    }

    /* (non-Javadoc)
     * @see net.sf.RecordEditor.utils.screenManager.ReFrame#executeAction(int, java.lang.Object)
     */
    @Override
    public void executeAction(int action, Object o) {
        BaseDisplay bd =  getActiveDisplay();

        if (bd != null && bd.getActionHandler().isActionAvailable(action)) {
            bd.getActionHandler().executeAction(action, o);
        } else {
            super.executeAction(action, o);
        }
    }

    /* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#executeAction(int)
     */
    @Override
    public void executeAction(int action) {
        executeAction(getActiveIdx(), action);
    }


	public void executeAction(AbstractFileDisplay screen, int action) {
		int idx = mainScreens.indexOf(screen);
		if (idx >= 0) {
			executeAction(idx, action);
		}
    }

    @Override
	public void executeAction(int idx, int action) {

        if (idx >= 0) {

			switch (action) { 
            case ReActionHandler.CLOSE_TAB:					close(idx);					break;
            case ReActionHandler.UNDOCK_TAB:				moveToSeperateScreen(idx);	break;
            case ReActionHandler.UNDOCK_ALL_TABS:			moveToSeperateScreen();		break;
            case ReActionHandler.DOCK_TAB:					addToMainTab(idx, true);	break;
            case ReActionHandler.DOCK_ALL_SCREENS:			dockAll();					break;
            case ReActionHandler.ADD_CHILD_SCREEN:
            	addChildScreen(idx, AbstractCreateChildScreen.CS_RIGHT);
            	break;
            case ReActionHandler.ADD_CHILD_SCREEN_RIGHT:
            	addChildScreen(idx, AbstractCreateChildScreen.CS_RIGHT);
            	break;
            case ReActionHandler.ADD_CHILD_SCREEN_BOTTOM:
            	addChildScreen(idx, AbstractCreateChildScreen.CS_BOTTOM);
            	break;
            case ReActionHandler.ADD_CHILD_SCREEN_SWAP:
            	if (idx >= 0 && idx < mainScreens.size()) {
            		int position = AbstractCreateChildScreen.CS_RIGHT;
            		if (mainScreens.get(idx).getCurrentChildScreenPostion() == AbstractCreateChildScreen.CS_RIGHT) {
            			position = AbstractCreateChildScreen.CS_BOTTOM;
            		}
            		addChildScreen(idx, position);
            	}
            	break;
            case ReActionHandler.REMOVE_CHILD_SCREEN:		removeChildScreen(idx);		break;
            default:
                AbstractFileDisplay bd =  getActiveDisplay();

                if (bd != null) {
                    if (bd.getActionHandler().isActionAvailable(action)) {
                    	bd.getActionHandler().executeAction(action);
                    }
                }
            }
        }
    }

    private void addChildScreen(int idx, int position) {

        if (idx >= 0 && idx < mainScreens.size()) {
            BaseDisplay bd = mainScreens.get(idx);
            if (bd.getFileView().getRowCount() == 0) {
                Common.logMsgRaw(ReMessages.EMPTY_VIEW.get(), null);
            } else if (bd instanceof AbstractCreateChildScreen) {
            	AbstractFileDisplay childDispl = ((AbstractCreateChildScreen) bd).createChildScreen(position);
                //childScreens.set(idx, childDispl);
                childDispl.setDockingPopup(bd.getDockingPopup());
                updateScreenStuff(idx);
            }
        }
    }

    private void removeChildScreen(int idx) {

        if (idx >= 0 && idx < mainScreens.size()) {
            mainScreens.get(idx).removeChildScreen();

            updateScreenStuff(idx);
        }
    }

    private void updateScreenStuff(int idx) {
        bldScreen();
        ReMainFrame.getMasterFrame().focusChanged(this);
        if (mainScreens.size() > 0) {
            mainScreens.get(0).setScreenSize(true);
        }
        if (pane != null) {
            pane.setSelectedIndex(idx);
        }
    }

    private void dockAll() {
        ReFrame prim = ReFrame.getPrimaryFrame(this.getDocument());
        ReFrame[] frames = ReFrame.getAllFrames();

        if (prim != null && prim instanceof DisplayFrame) {
            for (ReFrame f : frames) {
                if (f != this && f.getDocument() == this.getDocument() && f instanceof DisplayFrame) {
                    ((DisplayFrame) f).addToMainTab(prim);
                }
            }
            addToMainTab(prim);

            ((DisplayFrame) prim).bldScreen();
        }
    }


    private void addToMainTab(ReFrame prim) {

        if (prim != null && prim != this && prim instanceof DisplayFrame) {
            for (int i = 0; i < mainScreens.size(); i++) {
                addToMainTab(i, false);
            }
        }
    }

    private void addToMainTab(int idx, boolean rebuild) {
        ReFrame prim = ReFrame.getPrimaryFrame(this.getDocument());

        if (prim != null && prim != this && prim instanceof DisplayFrame) {
            BaseDisplay d = mainScreens.get(idx);

            removeIdx(idx);
            ((DisplayFrame) prim).addScreen(d, rebuild);

            if (mainScreens.size() == 0) {
                super.reClose();
            }
        }
    }

    /* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.IDisplayFrame#isActionAvailable(int)
     */
    @Override
    public boolean isActionAvailable(int action) {
        return isActionAvailable(getActiveIdx(), action);
    }

    @Override
	public boolean isActionAvailable(int idx, int action) {

        switch (action) {
        case ReActionHandler.CLOSE_TAB:
        case ReActionHandler.UNDOCK_TAB:
            return mainScreens.size() > 1 && idx > 0;
        case ReActionHandler.UNDOCK_ALL_TABS:
            return mainScreens.size() > 1;
        case ReActionHandler.ADD_CHILD_SCREEN:
            return     idx >= 0
                    && mainScreens.size() > idx
                    && mainScreens.get(idx).getChildScreen() == null
                    && mainScreens.get(idx) instanceof AbstractCreateChildScreen
                    && mainScreens.get(idx).getAvailableChildScreenPostion() != AbstractCreateChildScreen.CS_BOTH;
        case ReActionHandler.ADD_CHILD_SCREEN_RIGHT:
        case ReActionHandler.ADD_CHILD_SCREEN_BOTTOM:
            return     idx >= 0
                    && mainScreens.size() > idx
                    && mainScreens.get(idx).getChildScreen() == null
                    && mainScreens.get(idx) instanceof AbstractCreateChildScreen
                    && mainScreens.get(idx).getAvailableChildScreenPostion() == AbstractCreateChildScreen.CS_BOTH;
        case ReActionHandler.ADD_CHILD_SCREEN_SWAP:
            return     idx >= 0
                    && mainScreens.size() > idx
                    && mainScreens.get(idx).getChildScreen() != null
                    && mainScreens.get(idx) instanceof AbstractCreateChildScreen
                    && mainScreens.get(idx).getAvailableChildScreenPostion() == AbstractCreateChildScreen.CS_BOTH;
        case ReActionHandler.REMOVE_CHILD_SCREEN:
            return     idx >= 0
                    && mainScreens.size() > idx
                    && mainScreens.get(idx).getChildScreen() != null
                    && mainScreens.get(idx) instanceof AbstractCreateChildScreen;
        case ReActionHandler.DOCK_TAB:
            return this != ReFrame.getPrimaryFrame(this.getDocument());

        case ReActionHandler.DOCK_ALL_SCREENS:
            return true;
        default:
            if (idx >= 0 && idx < mainScreens.size()) {
                return (mainScreens.get(idx).getActionHandler().isActionAvailable(action));
            }
        }
        return false;
    }


    /* (non-Javadoc)
     * @see net.sf.RecordEditor.edit.display.common.ILayoutChanged#layoutChanged(net.sf.JRecord.Details.AbstractLayoutDetails)
     */
    @Override
    public void layoutChanged(AbstractLayoutDetails layout) {
        for (BaseDisplay bd : mainScreens) {
            bd.layoutChanged(layout);
        }
    }


    private class TabButton extends TabWithClosePnl implements ActionListener, IDisplayChangeListner {

        private final BaseDisplay disp;


        public TabButton(BaseDisplay display, boolean addCloseBtn) {
        	super(display.getScreenName(), addCloseBtn);
        	super.setCloseAction(this);

        	disp = display;

            disp.setChangeListner(this);

        	this.addMouseListener(disp.getDockingPopup());

            label.addMouseListener(disp.getDockingPopup());
        }


        @Override
        public void actionPerformed(ActionEvent ae ){

            int idx = pane.indexOfTabComponent( this );

            if (idx >= 0) {
                close(idx);
            }
        }

        /* (non-Javadoc)
         * @see net.sf.RecordEditor.edit.display.IDisplayChangeListner#displayChanged()
         */
        @Override
        public void displayChanged() {
            super.setTabname(disp.getScreenName());
        }
    }
}
