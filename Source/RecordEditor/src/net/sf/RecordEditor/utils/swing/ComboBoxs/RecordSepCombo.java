package net.sf.RecordEditor.utils.swing.ComboBoxs;

import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.lang.LangConversion;
import net.sf.RecordEditor.utils.swing.Combo.ComboKeyedOption;

@SuppressWarnings("serial")
public final class RecordSepCombo extends EnglishCombo<byte[]> {

	private static final String[] RECORD_SEPERATOR = {Common.DEFAULT_STRING, Common.CRLF_STRING, Common.CR_STRING, Common.LF_STRING};
	private static final String[] FOREIGN_NAMES = LangConversion.convertComboItms(
			"LayoutEdit_EndOfLine",
			RECORD_SEPERATOR.clone());
	private static final byte[][] RECORD_SEP_VALS  = {Common.CRLF_BYTES,     Common.CRLF_BYTES,  Common.CR_BYTES,  Common.LF_BYTES};

	private static ComboKeyedOption<byte[]> EMPTY = new ComboKeyedOption<byte[]>(new byte[]{}, "", "");

	public RecordSepCombo() {
		super(EMPTY);

		for (int i = 0; i < RECORD_SEPERATOR.length; i++) {
			super.addItem(new ComboKeyedOption<byte[]>(RECORD_SEP_VALS[i], FOREIGN_NAMES[i], RECORD_SEPERATOR[i]));
		}
	}

}
