package net.sf.RecordEditor.edit.display.Action;

import java.awt.event.ActionEvent;

import net.sf.RecordEditor.edit.open.DisplayBuilderFactory;
import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.re.script.AbstractFileDisplay;
import net.sf.RecordEditor.re.script.IDisplayBuilder;

import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.screenManager.AbstractActiveScreenAction;


@SuppressWarnings("serial")
public class ShowTextViewAction extends ReSpecificScreenAction implements AbstractActiveScreenAction {

	private final boolean selectedRecords;
	private final int screenType;

	public static ShowTextViewAction get(boolean selectedRecords, boolean coloredFields) {
		String s = "Text View";
		if (selectedRecords) {
			s = "Text View (Selected Records)";
		}
		int stype = IDisplayBuilder.ST_DOCUMENT;
		if (coloredFields) {
			stype = IDisplayBuilder.ST_COLORED_DOCUMENT;
			s = "Text View (highlight fields)";
			if (selectedRecords) {
				s = "Text View (Selected Records / highlight fields)";
			}
		}

		return new ShowTextViewAction(selectedRecords, s, stype);
	}
	/**
	 * @param creator
	 */
	private ShowTextViewAction(boolean selectedRecords, String msg, int sType) {
		super(msg);
		this.selectedRecords = selectedRecords;
		this.screenType = sType;

		checkActionEnabled();
	}

	/**
	 * @see net.sf.RecordEditor.utils.screenManager.AbstractActiveScreenAction#checkActionEnabled()
	 */
	@Override
	public void checkActionEnabled() {
		super.setEnabled(
				   Common.OPTIONS.allowTextEditting.isSelected()
				&& isActive(getDisplay(AbstractFileDisplay.class)));
	}

	@Override
	public void actionPerformed(ActionEvent arg0) {
		AbstractFileDisplay fileDisplay = getDisplay(AbstractFileDisplay.class);
		if (isActive(fileDisplay)) {
			FileView f = fileDisplay.getFileView();

			if (selectedRecords) {
				f = f.getView(fileDisplay.getSelectedLines());
			}

			if (f != null) {
				DisplayBuilderFactory.getInstance().newDisplay(screenType, "", fileDisplay.getParentFrame(), f.getLayout(), f, 0);
			}
		}
	}


	private boolean isActive(AbstractFileDisplay activeScreen) {
		boolean active = false;

		if (activeScreen != null) {
			AbstractFileDisplay source = (AbstractFileDisplay) activeScreen;
			active =  source.getFileView().isDocumentViewAvailable();
		}

		return active;
	}
}