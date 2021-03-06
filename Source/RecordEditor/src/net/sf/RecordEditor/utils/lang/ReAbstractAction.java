/**
 *
 */
package net.sf.RecordEditor.utils.lang;

import javax.swing.AbstractAction;
import javax.swing.Icon;

import net.sf.RecordEditor.utils.common.Common;

/**
 * Purpose: Foreign Language aware AbstractAction
 *
 * @author Bruce Martin
 * License GPL
 *
 */
@SuppressWarnings("serial")
public abstract class ReAbstractAction extends AbstractAction {

	/**
	 * @param name
	 */
	public ReAbstractAction(String name) {
		super(LangConversion.convert(LangConversion.ST_ACTION, name));

		putValue(AbstractAction.SHORT_DESCRIPTION, name);
	}

	/**
	 * @param name
	 * @param icon
	 */
	public ReAbstractAction(String name, Icon icon) {
		super(LangConversion.convert(LangConversion.ST_ACTION, name), icon);

		putValue(AbstractAction.SHORT_DESCRIPTION, name);
	}

	/**
	 * @param name
	 * @param icon
	 */
	public ReAbstractAction(String name, int iconId) {
		this(name, Common.getRecordIcon(iconId));
	}

}
