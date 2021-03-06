package net.sf.RecordEditor.re.script.extensions;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;

import net.sf.JRecord.Common.Conversion;

/**
 * Purpose Read Google Translations file back into an array list
 *
 * @author Bruce Martin
 *
 * License GPL
 *
 */
public class LanguageTrans {

	private ArrayList<String> list = new ArrayList<String>(1500);
	private static String BLANK = "";

	private static final String[] SUPPRESS_AFTER = {"<h1>", "<h2>", "<h3>", "<td>"};
	private static final String[] SUPPRESS_BEFORE = {"</h1>", "</h2>", "</h3>",};

	private static HashMap<String, LanguageTrans> translations = new HashMap<String, LanguageTrans>();


	public static LanguageTrans getTrans(String fname) {
		if (translations.containsKey(fname)) {
			return translations.get(fname);
		}

		LanguageTrans t = new LanguageTrans(fname);
		translations.put(fname, t);

		return t;
	}


	private LanguageTrans(String fileName) {

		try {
			BufferedReader r = new BufferedReader(new InputStreamReader(new FileInputStream(fileName), "UTF8"));
			String s, l = BLANK;
			boolean suppress = false;
			boolean suppressNext = false;
			int key = 0,  pos, pos2;


			for (int i = 0; i < 3000; i++) {
				list.add(BLANK);
			}
			while ((s = r.readLine()) != null) {
				if ("".equals(s.trim())) {

				} else {
					suppressNext = false;
					if (s.startsWith("::") || s.startsWith("：：")) {
						if (l != BLANK) {
							try {
								StringBuilder b = new StringBuilder(l);
								Conversion.replace(b, "</ ", "</");
								Conversion.replace(b, "\\n</h1", "</h1");
								Conversion.replace(b, "\\n</h2", "</h2");
								Conversion.replace(b, "\\n</h3", "</h3");
								list.set(key, b.toString());
								l = BLANK;
								key = 0;
							} catch (Exception e) {
								e.printStackTrace();
							}
						}
						pos = s.indexOf(":", 2);
						pos2 =  s.indexOf("：", 2);
						if (pos < 0) {
							pos =  pos2;
						} else if (pos2 >= 0) {
							pos = Math.min(pos, pos2);
						}
						if (pos > 2) {
							try {
								key = Integer.parseInt(s.substring(2, pos).trim());
								System.out.println("  >> " + key + " " + s);
								l = "";
								if (s.length() > pos + 2) {
									l = s.substring(pos + 1);
								}
							} catch (Exception e) {
								e.printStackTrace();
							}
						} else {
							System.out.println(" ## > " + pos + " " + s);
						}
						s = r.readLine();
						if (s == null) {
							break;
						}
						suppressNext = true;
					} else if (suppress || suppressBefore(s)) {
						l = l + s;
					} else {
						l = l + "\n" + s;
					}

					suppress = suppressNext;
					String t = s.toLowerCase();
					for (String ss : SUPPRESS_AFTER) {
						if (t.endsWith(ss)) {
							suppress = true;
							break;
						}
					}
				}
			}

			list.set(key, l);

			r.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private boolean suppressBefore(String s) {
		String t = s.toLowerCase();
		for (String ss : SUPPRESS_BEFORE) {
			if (t.startsWith(ss)) {
				return true;
			}
		}
		return false;
	}

	/**
	 * @param index
	 * @return
	 * @see java.util.ArrayList#get(int)
	 */
	public String get(int index) {
		return list.get(index);
	}

	public static void clear() {
		translations.clear();
	}
}
