/*
 * This class maanges the various line parsers
 */
package net.sf.JRecord.CsvParser;

import net.sf.JRecord.Common.BasicNamedManager;

/**
 * Class to manage the various CSV Line parsers
 * 
 * @author Bruce Martin
 */
public class ParserManager extends BasicNamedManager<AbstractParser> {
	
	public static final int BASIC_CSV_PARSER = 0;
	public static final int STANDARD_CSV_PARSER = 1;
	public static final int DB_CSV_PARSER = 2;
	
	private static final int NUMBER_OF_PARSERS = 10;
	private static ParserManager instance = null;
	
//	private Parser[] list = new Parser[NUMBER_OF_PARSERS];
//	private String[] names = new String[NUMBER_OF_PARSERS];
	
	/**
	 * Manage the various line parsers
	 *
	 */
	public ParserManager() {
		super(NUMBER_OF_PARSERS, NUMBER_OF_PARSERS, new AbstractParser[NUMBER_OF_PARSERS]);
		
		register(BASIC_CSV_PARSER, "Basic Parser", BasicParser.getInstance());
		register(STANDARD_CSV_PARSER, "Parser - Matching Quotes", new StandardParser());
		register(DB_CSV_PARSER, "Parser - Quotes based on field Type", new StandardParser(true));
	}


	/**
	 * get a ParserManager
	 * @return the instance
	 */
	public static ParserManager getInstance() {
		if (instance == null) {
			instance = new ParserManager();
		}
		return instance;
	}

	/**
	 * @see net.sf.JRecord.Common.BasicManager#get(int)
	 */
	@Override
	public AbstractParser get(int id) {
		if (id < 0 || id >= super.getNumberOfEntries()) {
			return super.get(0);
		}
		return super.get(id);
	}
	
	
}
