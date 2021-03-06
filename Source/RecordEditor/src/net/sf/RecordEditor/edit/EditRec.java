/*
 * @Author Bruce Martin
 * Created on 4/01/2007
 *
 * Purpose:
 *   Record Editor Main screen.
 *
 * Changes
 * # New Version 0.56 the old EditRec code was moved to OpenFile
 *
 * # Version 0.60 Bruce Martin 2007/02/16
 *   - new Data drop down menu
 *   - added support for reading user types from Parameter file
 *   - support for new java run program
 *   - support user_Initialise_class's added
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Support for User Date-Types
 *   - JRecord Spun off, code reorg
 */
package net.sf.RecordEditor.edit;

import java.awt.event.ActionEvent;
import java.io.File;

import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

import net.sf.JRecord.IO.AbstractLineIOProvider;
import net.sf.JRecord.Log.AbsSSLogger;
import net.sf.RecordEditor.edit.display.DisplayBuilderImp;
import net.sf.RecordEditor.edit.display.DisplayFrame;
import net.sf.RecordEditor.edit.display.Action.ChangeFileStructureAction;
import net.sf.RecordEditor.edit.display.Action.LoadSavedFieldSeqAction;
import net.sf.RecordEditor.edit.display.Action.LoadSavedVisibilityAction;
import net.sf.RecordEditor.edit.display.Action.ShowTextViewAction;
import net.sf.RecordEditor.edit.open.OpenCsvFileBackground;
import net.sf.RecordEditor.edit.open.OpenFile;
import net.sf.RecordEditor.edit.open.OpenReFileBackground;
import net.sf.RecordEditor.externalInterface.Plugin;
import net.sf.RecordEditor.re.jrecord.format.CellFormat;
import net.sf.RecordEditor.re.jrecord.types.ReTypeManger;
import net.sf.RecordEditor.re.jrecord.types.TypeDateWrapper;
import net.sf.RecordEditor.re.openFile.LayoutSelectionDB;
import net.sf.RecordEditor.re.script.ExportScriptPopup;
import net.sf.RecordEditor.re.script.RunScriptPopup;
import net.sf.RecordEditor.re.script.VelocityPopup;
import net.sf.RecordEditor.re.script.XsltPopup;
import net.sf.RecordEditor.re.script.bld.RunScriptSkelPopup;
import net.sf.RecordEditor.re.util.ReIOProvider;
import net.sf.RecordEditor.utils.CopyBookDbReader;
import net.sf.RecordEditor.utils.CopyBookInterface;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReActionHandler;
import net.sf.RecordEditor.utils.edit.ParseArgs;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.lang.ReAbstractAction;
import net.sf.RecordEditor.utils.params.Parameters;
import net.sf.RecordEditor.utils.params.ProgramOptions.ProgramType;
import net.sf.RecordEditor.utils.screenManager.AbstractActiveScreenAction;
import net.sf.RecordEditor.utils.screenManager.ReAction;
import net.sf.RecordEditor.utils.screenManager.ReActionActiveScreen;
import net.sf.RecordEditor.utils.screenManager.ReFrame;
import net.sf.RecordEditor.utils.screenManager.ReMainFrame;
import net.sf.RecordEditor.utils.swing.SwingUtils;

/**
 * Record Editor Main screen
 *
 * @author Bruce Martin
 *
 */
@SuppressWarnings("serial")
public class EditRec extends ReMainFrame  {

    private OpenFile open;
    private JMenu utilityMenu;
    private JMenu dataMenu;
    private JMenu viewMenu;
    private AbstractAction	newFileAction = null,
    						open2action = null,
    						new2action = null;

    private boolean incJdbc;
    private boolean includeWizardOptions = true;
    private AbstractAction optionAction = new ReAbstractAction(
    				"Edit Options",
    				Common.ID_PREF_ICON) {
        public void actionPerformed(ActionEvent e) {
        	editProperties(incJdbc, includeWizardOptions);
        }
	};
//    private CopyBookInterface copybookInterface;

	private final ReActionActiveScreen closeTabAction        = newAction(ReActionHandler.CLOSE_TAB);
	private final ReActionActiveScreen extractTabAction      = newAction(ReActionHandler.UNDOCK_TAB);
	private final ReActionActiveScreen extractAllAction      = newAction(ReActionHandler.UNDOCK_ALL_TABS);
	private final ReActionActiveScreen addToMainScreenAction = newAction(ReActionHandler.DOCK_TAB);
	private final ReActionActiveScreen toOneScreenAction     = newAction(ReActionHandler.DOCK_ALL_SCREENS);
	private final ReActionActiveScreen addChildRecAction     = newAction(ReActionHandler.ADD_CHILD_SCREEN);
	private final ReActionActiveScreen removeChildRecAction  = newAction(ReActionHandler.REMOVE_CHILD_SCREEN);

	private Action runScriptAction = addAction(new RunScriptAction());

    /**
     * Creating the File & record selection screenm
     *
     * @param pInFile File to be read (optional)
     * @param pInitialRow initinial Row (optional)
     * @param pInterfaceToCopyBooks interface to copybooks
     */
    public EditRec(final String pInFile,
                   final int pInitialRow,
                   final CopyBookInterface pInterfaceToCopyBooks) {
        this(pInFile, pInitialRow, ReIOProvider.getInstance(), pInterfaceToCopyBooks);
    }


    /**
     * Creating the File & record selection screenm
     *
     * @param pInFile File to be read (optional)
     * @param pInitialRow initinial Row (optional)
     * @param pIoProvider ioProvider to use when creating
     *        lines
     * @param pInterfaceToCopyBooks interface to copybooks
     */
    public EditRec(final String pInFile,
                   final int pInitialRow,
                   final AbstractLineIOProvider pIoProvider,
                   final CopyBookInterface pInterfaceToCopyBooks) {
       super("Record Editor", "", "re");

       checkVelocityScriptDir();
 //      copybookInterface = pInterfaceToCopyBooks;
       open = new OpenFile(pInFile,
                  pInitialRow,
                  pIoProvider,
                  null, null,
                  new LayoutSelectionDB(pInterfaceToCopyBooks, null, true));

        initMenusToolBars(true, null, null, null, null);
        setupMenus(null, null, null, null);
        EditCommon.doStandardInit();
     }


    /**
     * Creating the File & record selection screen
     *
     */
    public EditRec(final boolean includeJdbc) {
        this(includeJdbc, "Record Editor", null, null, null);
    }


    public EditRec(final boolean includeJdbc, final String name, AbstractAction newAction) {
    	this(includeJdbc, name, null, newAction, null);
    }


    private EditRec(final boolean includeJdbc, final String name,
    		AbstractAction open2Action, AbstractAction newAction, AbstractAction new2Action) {
    	super(name, "", "re");
    	checkVelocityScriptDir();

    	initMenusToolBars(includeJdbc, open2Action, newAction, new2Action, null);
    	EditCommon.doStandardInit();
    }

    public EditRec(final String name) {
    	super(name, "", "re");
    	checkVelocityScriptDir();
       	EditCommon.doStandardInit();
    }


    public EditRec(final boolean includeJdbc, final String name, String id, AbstractAction newAction, boolean loadAtBottom) {
    	super(name, "", id, loadAtBottom);
    	initMenusToolBars(includeJdbc, null, newAction, null, null);
     	EditCommon.doStandardInit();
    }
    


    /**
     * standard initialize
     *
     */
	protected final void initMenusToolBars(
			final boolean includeJdbc,
			AbstractAction open2Action,
			AbstractAction newAction, AbstractAction new2Action, 
			AbstractAction schemaEdit) {

    	this.newFileAction  = newAction;
    	this.open2action = open2Action;
    	this.new2action  = new2Action;
    	incJdbc = includeJdbc;

        updateMenus(newAction, schemaEdit);

        loadUserTypes();
        loadUserFormats();
 //       init_300_SetSizes();

//        init_200_SetSizes(loadAtBottom);

//        this.addWindowListener(new WindowAdapter() {
//            public void windowClosing(WindowEvent e) {
//                closeProcessing();
//            }
//
//            public void windowClosed(WindowEvent e) {
//                Common.closeConnection();
//
//                System.exit(0);
//            }
//        });
    }


	/**
	 * @param savedVisibiltyAction
	 * @param fieldSeqAction
	 * @param filterAction
	 * @param sortAction
	 */
	private void updateMenus( AbstractAction newAction,  AbstractAction schemaEdit) {
		
    	LoadSavedVisibilityAction savedVisibiltyAction = new LoadSavedVisibilityAction();
    	LoadSavedFieldSeqAction fieldSeqAction = new LoadSavedFieldSeqAction();
    	AbstractAction filterAction = newAction(ReActionHandler.FILTER);
    	AbstractAction sortAction = newAction(ReActionHandler.SORT);
    	ReActionActiveScreen autofitAction = newAction(ReActionHandler.AUTOFIT_COLUMNS);
    	Action[] toolbarActions = {	filterAction, sortAction,
    			autofitAction,
    			null,
    			runScriptAction,
    			optionAction
    	};
    	if (schemaEdit != null) {
    		Action[] tbAction = {filterAction, sortAction, filterAction, autofitAction,
    				null, 
    				schemaEdit,
    				null,
        			runScriptAction,
        			optionAction
    		};
    		toolbarActions = tbAction;
    	}

    	optionAction.putValue(AbstractAction.SHORT_DESCRIPTION, LangConversion.convert(LangConversion.ST_MESSAGE, "Edit Options"));

    	DisplayBuilderImp.register();

        ReMainFrame.setMasterFrame(this);
        ReTypeManger.setDateFormat(Common.DATE_FORMAT_STR);

        buildMenubar(VelocityPopup.getPopup(), XsltPopup.getPopup(), ExportScriptPopup.getPopup());
        buildToolbar(newAction, toolbarActions);
        
		dataMenu.add(filterAction);
        dataMenu.add(newAction(ReActionHandler.TABLE_VIEW_SELECTED));
        dataMenu.add(sortAction);
        dataMenu.add(newAction(ReActionHandler.REBUILD_TREE));
        dataMenu.addSeparator();
        dataMenu.add(newAction(ReActionHandler.ADD_ATTRIBUTES));
        dataMenu.addSeparator();
        dataMenu.add(newAction(ReActionHandler.FULL_TREE_REBUILD));

        dataMenu.addSeparator();
        dataMenu.add(addAction(new ChangeFileStructureAction()));

        viewMenu.add(newAction(ReActionHandler.BUILD_FIELD_TREE));
        viewMenu.add(newAction(ReActionHandler.BUILD_SORTED_TREE));
        viewMenu.add(newAction(ReActionHandler.BUILD_RECORD_TREE));
        viewMenu.addSeparator();
        viewMenu.add(newAction(ReActionHandler.BUILD_LAYOUT_TREE));
        viewMenu.add(newAction(ReActionHandler.BUILD_LAYOUT_TREE_SELECTED));

        boolean allowTextView = Common.OPTIONS.addTextDisplay.isSelected()
        					 && Common.OPTIONS.allowTextEditting.isSelected();
        //Common.logMsg(" Add Text Display: " + Common.OPTIONS.addTextDisplay.isSelected(), null);
        if (allowTextView) {
            viewMenu.addSeparator();
            viewMenu.add(addAction(ShowTextViewAction.get(false, false)));
            viewMenu.add(addAction(ShowTextViewAction.get(false, true)));
       }
        viewMenu.addSeparator();
        viewMenu.add(newAction(ReActionHandler.TABLE_VIEW_SELECTED));
        viewMenu.add(newAction(ReActionHandler.RECORD_VIEW_SELECTED));
        viewMenu.add(newAction(ReActionHandler.COLUMN_VIEW_SELECTED));
        viewMenu.add(newAction(ReActionHandler.SELECTED_VIEW));
        viewMenu.add(newAction(ReActionHandler.BUILD_XML_TREE_SELECTED));
        if (allowTextView) {
             viewMenu.add(addAction(ShowTextViewAction.get(true, false)));
             viewMenu.add(addAction(ShowTextViewAction.get(true, true)));
        }

        viewMenu.addSeparator();
        viewMenu.add(newAction(ReActionHandler.EXECUTE_SAVED_FILTER));
        viewMenu.add(newAction(ReActionHandler.EXECUTE_SAVED_SORT_TREE));
        viewMenu.add(newAction(ReActionHandler.EXECUTE_SAVED_RECORD_TREE));
        addAction(savedVisibiltyAction);
        addAction(fieldSeqAction);
        viewMenu.add(savedVisibiltyAction);
        viewMenu.add(fieldSeqAction);



        runInitClass(Common.USER_INIT_CLASS, "Error running user Initialize:");

        if (Common.OPTIONS.loadPoScreens.isSelected()) {
        	runInitClass(Common.PO_INIT_CLASS, null);
        }

        //runInitClass(Common.USER_INIT_CLASS, "Error running user GetText Init");

//        if (Common.USER_INIT_CLASS != null && ! "".equals(Common.USER_INIT_CLASS)) {
//            try {
//                @SuppressWarnings("rawtypes")
//				Class c = ClassLoader.getSystemClassLoader().loadClass(Common.USER_INIT_CLASS);
//                if (c != null) {
//                	c.newInstance();
//                }
//            } catch (Exception e) {
//                Common.logMsg(
//                		AbsSSLogger.ERROR,
//                		"Error running user Initialize:",
//                        e.getMessage(),
//                        null);
//            }
//        }
	}


	@Override
    protected void removeSpecificMenus() {
    	removeSpecificMenus(11);
    }

	@Override
    protected void addSpecificWindows(JMenu winMenu, ReAction closeAction) {

        winMenu.addSeparator();
        winMenu.add(extractTabAction);
        winMenu.add(extractAllAction);
        winMenu.add(addToMainScreenAction);
        winMenu.add(toOneScreenAction);
        winMenu.addSeparator();
        winMenu.add(addChildRecAction);
        winMenu.add(removeChildRecAction);
        winMenu.addSeparator();
        winMenu.add(closeTabAction);
        winMenu.add(closeAction);
    }


    /**
     * Build File menu
     * @param compareAction compare action
     */
    private void setupMenus(Action copyAction, Action compareAction, JMenuItem compareMenu, JMenuItem newMenuItem) {
    	JMenu  em;

        buildFileMenu(
        		open.getOpenFilePanel().getRecentFileMenu(),
        		open.getOpenFilePanel().getRecentDirectoryMenu(),
        		true, false,
        		newMenuItem,
        		open2action,
        		newFileAction,
        		new2action);

        if (copyAction != null) {
        	utilityMenu.add(new ReAbstractAction("Cobol Copybook Analysis") {
					@Override public void actionPerformed(ActionEvent e) {
						new net.sf.RecordEditor.edit.display.DisplayCobolCopybook();
					}
		        });
        	utilityMenu.addSeparator();
	        utilityMenu.add(copyAction);
	        utilityMenu.addSeparator();
	    }
        utilityMenu.add(newAction(ReActionHandler.COMPARE_WITH_DISK));
        if (compareAction != null) {
        	utilityMenu.add(compareAction);
        }
        if (compareMenu != null) {
        	utilityMenu.add(compareMenu);
        }
        utilityMenu.addSeparator();

        JMenu bldMenu = RunScriptSkelPopup.buildScriptMenu(null, "Script Build");
		if (bldMenu != null) {
			utilityMenu.add(bldMenu);
		}
        utilityMenu.add(RunScriptPopup.getPopup());
		utilityMenu.add(runScriptAction);

        em = getEditMenu();
	    em.addSeparator();
	    em.add(optionAction);
	    
	    //resizeFrame();

        super.addExit();
   }


	/**
	 * Add program specific dropdown menus
	 * @param menubar top level menu
	 */
	protected void addProgramSpecificMenus(JMenuBar menubar) {
		utilityMenu = SwingUtils.newMenu("Utilities");
	    dataMenu = SwingUtils.newMenu("Data");
	    viewMenu = SwingUtils.newMenu("View");

        menubar.add(utilityMenu);
        menubar.add(dataMenu);
        menubar.add(viewMenu);

        loadUserFunctions(menubar);
	}

	private void loadUserFunctions(JMenuBar menubar) {
		Object[] userFunctions = Common.readPropertiesArray(Parameters.PROPERTY_PLUGIN_FUNC_CLASS,
				Parameters.NUMBER_OF_USER_FUNCTIONS);

		if (userFunctions != null) {
			JMenu localMenu = SwingUtils.newMenu("Plugin");
			String name, param;
			Plugin userClass;
			int j = 0;

			for (int i = 0; i < Parameters.NUMBER_OF_USER_FUNCTIONS; i++) {
				if (userFunctions[i] != null) {
					try {
						userClass = (Plugin) userFunctions[i];
						name = Parameters.getString(Parameters.PROPERTY_PLUGIN_FUNC_NAME + i);
						param = Parameters.getString(Parameters.PROPERTY_PLUGIN_FUNC_PARAM + i);
						localMenu.add(new LocalAction(name, userClass, param));
						j += 1;
					} catch (Exception e) {
						Common.logMsg(AbsSSLogger.ERROR, "Error loading Function", e.getMessage(), e);
					}
				}
			}

			if (j > 0) {
				menubar.add(localMenu);
			}
		}

	}


    /**
     * Load user defined types
     *
     */
    public static void loadUserTypes() {
        int i, typeNum, baseType;
        ReTypeManger sysTypes = ReTypeManger.getInstance();
        net.sf.JRecord.Types.Type newType;
        String name, format, baseTypeStr;
        CellFormat newFormat;
        int[] typeIds = Common.readIntPropertiesArray(Parameters.TYPE_NUMBER_PREFIX, Parameters.NUMBER_OF_TYPES);
        Object[] types = Common.readPropertiesArray(typeIds, Parameters.TYPE_CLASS_PREFIX);

        if (types != null) {
            Object[] formats = Common.readPropertiesArray(typeIds, Parameters.TYPE_FORMAT_PREFIX);
            for (i = 0; i < Parameters.NUMBER_OF_TYPES; i++) {
                if (types[i] != null) {
                    try {
                        newType = (net.sf.JRecord.Types.Type) types[i];
                        if (formats == null || formats[i] == null) {
                            sysTypes.registerType(typeIds[i], newType);
                        }  else {
                             newFormat = (CellFormat) formats[i];
                             //System.out.println("~~~> " + newFormat.getClass().getName());
                             sysTypes.registerType(typeIds[i], newType, newFormat);
                        }
                    } catch (Exception e) {
                        Common.logMsg("Error Defining Type > " + typeIds[i]
                                    + " class=" + Parameters.getString(Parameters.TYPE_CLASS_PREFIX + i)
                                    + "  " + e.getMessage(), e);
                    }
                }
            }
        }

        // Define User Date Types
        for (i = 0; i < Parameters.DATE_TYPE_TABLE_SIZE; i++) {
		    name = Parameters.getString(Parameters.PROPERTY_DATE_TYPE_NAME + i);
		    format = Parameters.getString(Parameters.PROPERTY_DATE_FORMAT + i);
		    baseTypeStr = Parameters.getString(Parameters.PROPERTY_DATE_BASE_TYPE + i);
		    if (name   != null && ! "".equals(name)
		    &&  format != null && ! "".equals(format)
		    &&  baseTypeStr != null && ! "".equals(baseTypeStr)) {
		        try {
		            typeNum = Parameters.FIRST_USER_DATE_TYPE + i;
		            baseType = Integer.parseInt(baseTypeStr);
		            newFormat = ReTypeManger.getFormatFor(format);

		            newType = new TypeDateWrapper(sysTypes.getType(baseType), format);

		            sysTypes.registerType(typeNum, newType, newFormat);
                } catch (Exception e) {
                    Common.logMsg("Error Defining Type > " + name
                                + "  " + e.getMessage(), e);
                }
		    }
		}

    }

    public static void loadUserFormats() {

    	int i;
    	CellFormat fmt;
    	ReTypeManger sysTypes = ReTypeManger.getInstance();
        int[] formatIds = Common.readIntPropertiesArray(Parameters.FORMAT_NUMBER_PREFIX, Parameters.NUMBER_OF_FORMATS);
        Object[] formats = Common.readPropertiesArray(formatIds, Parameters.FORMAT_CLASS_PREFIX);

        if (formats != null) {
            for (i = 0; i < Parameters.NUMBER_OF_FORMATS; i++) {
            	if (formats[i] != null) {
            		try {
            			fmt = (CellFormat) formats[i];
            			sysTypes.registerFormat(formatIds[i], fmt);
            		} catch (Exception e) {
            			Common.logMsgRaw(
            					LangConversion.convertMsg(
            							"Error Defining Type > {0} class={1} {2}",
            							new Object[] {
            									formatIds[i],
            									Parameters.getString(Parameters.TYPE_CLASS_PREFIX + i),
            									e.getMessage()}),
            					e);
            		}
            	}
            }
        }

    }




    /**
     * @see net.sf.RecordEditor.utils.common.ReActionHandler#executeAction(int)
     */
    public void executeAction(int action) {

        switch (action) {
            case ReActionHandler.OPEN:
                //System.out.println("--->");
            	ReActionHandler activeFrame = ReFrame.getActiveFrame();
        		if (activeFrame != null && activeFrame.isActionAvailable(ReActionHandler.OPEN)) {
        			activeFrame.executeAction(ReActionHandler.OPEN);
        		} else if (open.isVisible()) {
        			ReFrame.moveFrameToFront(open);
        		} else {
        			open.setVisible(true);
        			ReFrame.moveFrameToFront(open);

//	                open.moveToFront();
//	                open.setVisible(true);
//	                open.setTheBounds();
//	                open.requestFocus();
//					try {
//						open.setMaximum(false);
//						open.setSelected(true);
//					} catch (PropertyVetoException e) {
//						e.printStackTrace();
//					}
        		}
                break;
            default:
        }
    }

    /**
     * @see net.sf.RecordEditor.utils.common.ReActionHandler#isActionAvailable(int)
     */
    public boolean isActionAvailable(int action) {
        return action == ReActionHandler.OPEN
            || super.isActionAvailable(action);
    }


    /**
     * @return Returns the open.
     */
    public OpenFile getOpenFileWindow() {
        return open;
    }

    /**
     * @param openWindow The open to set.
     */
    protected void setOpenFileWindow(OpenFile openWindow,
    		Action copyAction,
    		Action compareAction,
    		JMenuItem newMenuItem,
    		boolean incWizard) {
        this.open = openWindow;

        includeWizardOptions = incWizard;
        setupMenus(copyAction, compareAction, null, newMenuItem);
    }

    /**
     * @param openWindow The open to set.
     */
    protected void setOpenFileWindow(OpenFile openWindow,
    		Action copyAction,
    		JMenuItem compareMenu,
    		JMenuItem newMenuItem,
    		boolean incWizard) {
        this.open = openWindow;

        includeWizardOptions = incWizard;
        setupMenus(copyAction, null, compareMenu, newMenuItem);
    }
   /**
	 * @return the viewMenu
	 */
	public final JMenu getViewMenu() {
		return viewMenu;
	}


    protected void editProperties(boolean includeJdbc, boolean includeWizardOptions) {
    	new net.sf.RecordEditor.re.editProperties.EditOptions(false, includeJdbc, includeWizardOptions);
    }

	/**
     * This Class Executes a user written function. It is initiated from
     * the Local Dropdown Menu
     *
     * @author Bruce Martin
     *
     */
    public static class LocalAction extends AbstractAction {

    	private Plugin extension = null;
    	private String param;

    	public LocalAction(String name, Plugin userClass, String userParam) {
    		super(name);
    		extension = userClass;
    		param = userParam;
    	}

    	@Override
    	public void actionPerformed(ActionEvent event) {

    	    ReFrame actionHandler = ReFrame.getActiveFrame();
    	    if (actionHandler != null && actionHandler instanceof DisplayFrame) {
    	    	try {
    	    		net.sf.RecordEditor.re.display.AbstractFileDisplay display = ((DisplayFrame) actionHandler).getActiveDisplay();
    	    		extension.execute(param, display.getFileView(), display.getSelectedRows());
    	    	} catch (Exception e) { }
    	    }
    	}

    }

	private static class RunScriptAction extends ReAbstractAction implements AbstractActiveScreenAction {
		public RunScriptAction() {
			super("Script Test Panel",  Common.ID_SCRIPT_ICON);
		}

		@Override
		public void actionPerformed(ActionEvent e) {
			new net.sf.RecordEditor.re.script.runScreen.ScriptRunFrame();
		}

		/* (non-Javadoc)
		 * @see net.sf.RecordEditor.utils.screenManager.AbstractActiveScreenAction#checkActionEnabled()
		 */
		@Override
		public void checkActionEnabled() {
			setEnabled(ReFrame.getActiveFrame() instanceof DisplayFrame);
		}
	}

	 protected static void checkVelocityScriptDir() {
		 File f = new File(Common.OPTIONS.velocityScriptDir.get());
		 File zip = new File(Parameters.getSytemJarFileDirectory() + "/VelocityScript.zip");
		 System.out.println("--}}} " + f.getPath() + " " + zip.getPath()
				 + " " + f.exists() + " " + zip.exists());
		 if (! f.exists() && zip.exists()) {
			 new Thread(new Runnable() {
				@Override public void run() {
					 try {
						String destDir = Common.OPTIONS.velocityScriptDir.get();
			
						File f = new File(destDir);
						File destParent = f.getParentFile();
						
						Common.createDirectory(destParent);
						if (! destParent.exists()) {
							destParent.createNewFile();
							//Files.createDirectories(destParent.toPath());
						}
						// Fully qualifying so the whole class is not dependent on
						// net.lingala.zip4j.core.ZipFile
						net.lingala.zip4j.core.ZipFile zipFile = new net.lingala.zip4j.core.ZipFile(
								Parameters.getSytemJarFileDirectory() + "/VelocityScript.zip");
						zipFile.extractAll(destDir);
					} catch (Exception e) {
						e.printStackTrace();
					}
				}
			}).start();
		 }
	 }
    /**
     * Edit a record oriented file
     * @param pgmArgs program arguments
     */
    public static void main(final String[] pgmArgs) {

        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                //JFrame.setDefaultLookAndFeelDecorated(true);
    			Common.OPTIONS.programType = ProgramType.RECORD_EDITOR;

                ParseArgs args = new ParseArgs(pgmArgs);
                Common.setReadOnly(true);
                new EditRec(args.getDfltFile(), args.getInitialRow(),
                        CopyBookDbReader.getInstance());
                OpenCsvFileBackground.register();
                OpenReFileBackground.register();
            }
        });
    }
}
