If you have ant installed, you can compile the package by going into the RecordEditor directory and typing in 
ant. This will compile cb2xml, JRecord and RecordEDitor. The output jars will be in the newly created lib directories
in cb2xml, JRecord and RecordEditor directories. 
Before you can run the ant compile you must copy the following files from your RecordEditor install
to the lib directory associated with this zip file !!!!!
  - velocity-1.7.jar (lib/velocity-1.7.jar) - Velocity: available in your RecordEditor Install
  - velocity-1.7-dep.jar


Supplied Source Directories

   cb2xml       - holds my version of cb2xml - Cobol Copybook analysis 
   JRecord_Common - Low level IO and line representation code that is shared with the JRecord
   JRecord      - Mid level IO and line representation code
   RecordEditor - Source for the editor
   re_utilities - RecordEditor utilities holds JUnit tests + some example code.
   ZCalendar    - Date Display jar + lowlevel ComboPopup code.
   RecordEditor_Tests - Tests


------------------------------------------------------------------------------------------------------------------
 
To Compile The recordEditor you will need

      hsqldbmain.jar   (lib/hsqldbmain.jar)   - there is specific coding for the HSQL DB
      jibx-run.jar     (lib/jibx-run.jar)     - XML bidings for saving / restoring parameter files
      jlibdiff.jar     (lib/jlibdiff.jar)     - File Compare
      TableLayout.jar  (lib/TableLayout.jar)  - Screen Layout
      velocity-1.7.jar (lib/velocity-1.7.jar) - Velocity: available in your RecordEditor Install
      velocity-1.7-dep.jar (lib/velocity-1.7-dep.jar) - Velocity: available in your RecordEditor Install

      ZCalanedar either    the source in src/ZCalendar                or lib/ZCalendar.jar - Displaying dates 
      cb2xml     either    the source in src/cb2xml/src directory     or lib/cb2xml.jar    - Cobol Copybooks code

      JRecord Source (in the src/JRecord/src directory)            - Low level access / IO Code
      RecordEditor  Source for the Record Editor

to compile just run the supplied build.bat/build.sh scripts


------------------------------------------------------------------------------------------------------------------
 Other Supplied Source

       src/re_utilities    holds some old utilities + JUnit Tests
       src/AvroEditor      holds code for Editing Avro Binary files, will become a seperate project at some stage


------------------------------------------------------------------------------------------------------------------

1 final point, if you wish to work with the cource in IDE you will need to

1) Add you JDBC jar to the IDE as an external jar
2) Add the various utility libraries above to the IDE
3) Update net/sf/RecordEditor/utils/RecEdit.properties to point at your instalation (can copy from lib/properties.zip)

YIt will probably be easiest to work with a HSQL version as it is setup for this already (just start the HSQLDB server)