/*
 * @Author Bruce Martin
 * Created on 22/03/2007
 *
 * Purpose:
 */
package net.sf.RecordEditor.utils.swing;

/**
 * table rendor for 3 line hex display
 *
 * @author Bruce Martin
 *
 */
public class HexThreeLineRender extends HexGenericRender  {
    /**
     * @param font fontname
     */
    public HexThreeLineRender(final String font) {
        super(font, new HexThreeLineField(font));
    }
}
