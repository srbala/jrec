package net.sf.RecordEditor.re.file;

import java.util.Iterator;
import java.util.List;

import javax.swing.JOptionPane;

import net.sf.JRecord.Details.AbstractLine;
import net.sf.RecordEditor.utils.ExpandLineTree;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.lang.ReOptionDialog;

public abstract class PositionIncrement {

	public final FilePosition pos;
	protected final List<? extends AbstractLine> lines;

	private boolean endOfFileChk = true, eofFound = false;

	/**
	 * Get class to increment position
	 * @param position position to be updated
	 * @param allLines all the lines in the view
	 * @return increment class
	 */
	public static PositionIncrement newIncrement(FilePosition position, List<? extends AbstractLine> allLines, boolean endOfFileChk) {
		PositionIncrement ret;

		if (position.currentLine != null) {
			Iterator<AbstractLine> it;
			if (position.isForward()) {
				it = new TreeIteratorForward(allLines, position.currentLine);
			} else {
				it = new TreeIteratorBackward(allLines, position.currentLine);
			}

			if (position.isReadPending() && it.hasNext()) {
				position.currentLine = it.next();
				position.setReadPending(false);
			}

			if (position.getFieldId() == Common.ALL_FIELDS) {
				ret = new AllFieldsIterator(position, allLines, it);
			} else {
				ret = new SpecificFieldIterator(position, allLines, it);
			}
		} else if (position.getFieldId() == Common.ALL_FIELDS) {
			ret = new AllFields(position, allLines);
		} else {
			ret = new SpecificField(position, allLines);
		}

		ret.endOfFileChk = endOfFileChk;
		return ret;
	}



	private PositionIncrement(FilePosition position,
			List<? extends AbstractLine> allLines) {
		pos = position;
		lines = allLines;
	}

	public boolean isValidPosition() {

		if (iIsValidPosition()) {
			return true;
		}

		if (endOfFileChk) {
			if (eofFound) {
				ReOptionDialog.showMessageDialog(null, "Not found in the view");
				
				return false;
			} 
			
			eofFound = true;

			int opt = ReOptionDialog.showConfirmDialog(null, getMsg(), "", JOptionPane.YES_NO_OPTION);

			if (opt == JOptionPane.YES_OPTION) {
				pos.gotoStart();
				nextPosition();

				return iIsValidPosition();
			}
		}
		return false;
	}



	/**
	 * @param endOfFileChk the endOfFileChk to set
	 */
	public final void setEndOfFileChk(boolean endOfFileChk) {
		this.endOfFileChk = endOfFileChk;
	}



	/**
	 * @return
	 */
	private String getMsg() {
		String s;
		if (pos.isForward()) {
			s = "Reached the end of the file, do you want search from the start ??";
		} else {
			s = "Reached the Start of the file, do you want search from the end ??";
		}
		return s;
	}



	protected boolean iIsValidPosition() {
		return pos.row < lines.size() && (pos.row >= 0);
	}

	/**
	 * get the maximum field number + adjust position
	 * @return maximum field number
	 */
	protected int getMaxField() {
		if (pos.row >= lines.size() || pos.row < 0) {
			return -1;
		}

		AbstractLine currLine = lines.get(pos.row);
        if (pos.currentLine != null) {
        	currLine = pos.currentLine;
        }
        int prefIdx = currLine.getPreferredLayoutIdx();
        if (prefIdx < 0 || prefIdx >= currLine.getLayout().getRecordCount()) {
        	return -1;
        }
        int maxField = currLine.getLayout().getRecord(prefIdx).getFieldCount();

        pos.recordId = prefIdx;

        if (! pos.isValidFieldNum(maxField)) {
            pos.currentFieldNumber = maxField - 1;
            if (pos.isForward()) {
                pos.currentFieldNumber = 0;
            }
        }
        return maxField;
	}

	public abstract FilePosition nextPosition() ;



	private final static class SpecificField extends PositionIncrement {
		private SpecificField(FilePosition position, List<? extends AbstractLine> allLines) {
			super(position, allLines);
			
			if (! position.isValidFieldNum(getMaxField())) {
				pos.nextRow();
			}
		}

		public FilePosition nextPosition() {
			pos.nextRow();

			return pos;
		}
	}


	private final static class AllFields extends PositionIncrement  {
		int maxField;
		private AllFields(FilePosition position, List<? extends AbstractLine> allLines) {
			super(position, allLines);
			maxField = getMaxField();
			checkField();
		}

		/**
		 * @see net.sf.RecordEditor.re.file.PositionIncrement#iIsValidPosition
		 */
		@Override
		protected boolean iIsValidPosition() {
			return super.iIsValidPosition()
			  || (pos.isValidFieldNum(maxField));
		}

		public FilePosition nextPosition() {

			pos.nextField();
			checkField();

			return pos;
		}

		private void checkField() {

			if (! pos.isValidFieldNum(maxField)) {
				pos.nextRow();
				maxField = getMaxField();
			}
		}

	}

	private abstract static class IteratorInc extends PositionIncrement {
		private Iterator<AbstractLine> it;
		private boolean valid = true;

		public IteratorInc(FilePosition position,
				List<? extends AbstractLine> allLines,
				Iterator<AbstractLine> iterator) {
			super(position, allLines);

			it = iterator;
		}

		/**
		 * @see net.sf.RecordEditor.re.file.PositionIncrement#iIsValidPosition()
		 */
		@Override
		protected final boolean iIsValidPosition() {
			return valid;
		}


		public FilePosition nextRow() {
			AbstractLine l;
			if (it.hasNext()) {
				do {
					l = it.next();
					pos.currentLine = l;
				} while (pos.currentLine != null
						&& ( l.getLayout().getRecord(l.getPreferredLayoutIdx()).getFieldCount() == 0)
							||	(pos.currentLine.getPreferredLayoutIdx() != pos.recordId
							&& pos.getFieldId() >= 0
							&& it.hasNext()));

//				if (it.hasNext()) {
					int row = lines.indexOf(ExpandLineTree.getRootLine(pos.currentLine));
					//System.out.println("~~ row: " + row);
					if (row >= 0) {
//						if (row == 89) {
//							System.out.println("~~ row: " + row);
//						}
						pos.row = row;
					}
//				} else {
					valid = it.hasNext();
//				}
					pos.resetCol();
			} else {
				valid = false;
			}

			return pos;
		}

	}

	private static class SpecificFieldIterator extends IteratorInc {

		private SpecificFieldIterator(FilePosition position,
				List<? extends AbstractLine> allLines,
				Iterator<AbstractLine> iterator) {
			super(position, allLines, iterator);
		}

		public FilePosition nextPosition() {
			return nextRow();
		}
	}



	private static class AllFieldsIterator extends IteratorInc {
		int maxField;

		private AllFieldsIterator(
				FilePosition position,
				List<? extends AbstractLine> allLines,
				Iterator<AbstractLine> iterator) {
			super(position, allLines, iterator);
			maxField = getMaxField();
			checkRow();
		}

		public FilePosition nextPosition() {

			pos.nextField();
			checkRow();

			return pos;
		}

		private void checkRow() {

			if (! pos.isValidFieldNum(maxField)) {
				pos.nextRow();
				nextRow();
				maxField = getMaxField();
			}
		}
	}

}
