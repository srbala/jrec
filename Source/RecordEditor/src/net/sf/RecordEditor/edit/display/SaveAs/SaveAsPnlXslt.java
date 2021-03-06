/**
 *
 */
package net.sf.RecordEditor.edit.display.SaveAs;

import java.io.File;
import java.io.OutputStream;
import java.net.URL;
import java.net.URLClassLoader;

import net.sf.RecordEditor.re.file.FileView;
import net.sf.RecordEditor.re.openFile.RecentFiles;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.params.Parameters;
import net.sf.RecordEditor.utils.swing.BasePanel;
import net.sf.RecordEditor.utils.swing.treeCombo.FileSelectCombo;

/**
 * @author Bruce Martin
 *
 */
public class SaveAsPnlXslt extends SaveAsPnlBase {

	private FileSelectCombo xsltJar1 = new FileSelectCombo(Parameters.XSLT_JAR_LIST, 15, true, false);
			//new FileChooser(true, "Choose Jar");
	private FileSelectCombo xsltJar2 = new FileSelectCombo(Parameters.XSLT_JAR_LIST, 15, true, false);

	/**
	 * @param extension
	 * @param panelFormat
	 * @param extensionType
	 * @param template
	 */
	public SaveAsPnlXslt(CommonSaveAsFields commonSaveAsFields) {
		super(commonSaveAsFields, ".xml", CommonSaveAsFields.FMT_XSLT, RecentFiles.RF_XSLT, 
				new FileSelectCombo(Parameters.XSLT_LIST, 25, true, false), false);
		//new FileChooser(true, "get Xslt"));

		panel.addLineRE("Xslt Engine (leave blank for default)", xsltTxt);
        panel.addLineRE("Xslt File", template);
		panel.setGapRE(BasePanel.GAP1);

        panel.addLineRE("Jars", xsltJar1);
        panel.addLineRE("", xsltJar2);

		xsltTxt.setText(Common.OPTIONS.XSLT_ENGINE.get());

		template.setText(Common.OPTIONS.DEFAULT_XSLT_DIRECTORY.get());
		xsltJar1.setText(Common.OPTIONS.XSLT_JAR1.get());
		xsltJar2.setText(Common.OPTIONS.XSLT_JAR2.get());

		template.addFcFocusListener(commonSaveAsFields.templateListner);
     }

	public void save(String selection, OutputStream outFile) throws Exception {
    	//TODO Xslt Processing
    	//TODO Xslt Processing
    	//TODO Xslt Processing
    	javax.xml.transform.Source xmlSource, xsltSource;
    	javax.xml.transform.Result result;
    	javax.xml.transform.TransformerFactory transFact;
    	javax.xml.transform.Transformer trans;

    	FileView view = commonSaveAsFields.getViewToSave(selection);


    	File tempFile = File.createTempFile("reXsltInput", ".xml");
    	String xsltFileName = template.getText(),
    	       xsltClass = xsltTxt.getText();


    	view.writeFile(tempFile.getCanonicalPath());

		xmlSource = new javax.xml.transform.stream.StreamSource(tempFile);
		xsltSource = new javax.xml.transform.stream.StreamSource(xsltFileName);
		result = new javax.xml.transform.stream.StreamResult(outFile);

		Parameters.setSavePropertyChanges(false);
		Common.OPTIONS.XSLT_ENGINE.set(xsltClass);
		Common.OPTIONS.XSLT_JAR1.set(xsltJar1.getText());
		Parameters.setSavePropertyChanges(true);
		Common.OPTIONS.XSLT_JAR2.set(xsltJar2.getText());

		if ("".equals(xsltClass)) {
			transFact = javax.xml.transform.TransformerFactory.newInstance();
		} else {
			ClassLoader classLoader = this.getClass().getClassLoader();
			String jar1 = xsltJar1.getText(),
				   jar2 = xsltJar2.getText();
			if ("saxon".equalsIgnoreCase(xsltClass)) {
				xsltClass = "net.sf.saxon.TransformerFactoryImpl";
			} else if ("xalan".equalsIgnoreCase(xsltClass)) {
				xsltClass = "org.apache.xalan.processor.TransformerFactoryImpl";
			}

			if ((! "".equals(jar1)) || (! "".equals(jar2))) {
				int count = 2;
				String urlStr[] = {jar1, jar2};
				int idx = 0;
				if (("".equals(jar1)) || ("".equals(jar2))) {
					count = 1;
				}
				URL[] urls = new URL[count];
				for (int i = 0 ; i < urlStr.length; i++) {
					if (! "".equals(urlStr[i])) {
						urls[idx++] = (new File(urlStr[i])).toURI().toURL();
					}
				}

				classLoader =  new URLClassLoader(urls);
			}
			transFact = javax.xml.transform.TransformerFactory
							 .newInstance(xsltClass, classLoader);
		}

		trans = transFact.newTransformer(xsltSource);

		trans.transform(xmlSource, result);
	}


	/**
	 * @see net.sf.RecordEditor.edit.display.SaveAs.SaveAsPnlBase#isActive()
	 */
	@Override
	public boolean isActive() {
		return Common.OPTIONS.xsltAvailable.isSelected();
	}
}
