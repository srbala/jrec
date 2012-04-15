; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
SetCompressor /SOLID lzma
SetCompressionLevel 9

!define PRODUCT_NAME "RecordEdit_HSQL"                                                             
!define PRODUCT_VERSION "0.80.6"                                                                                  
!define PRODUCT_PUBLISHER "Bruce Martin"                                                           
!define PRODUCT_WEB_SITE "http://record-editor.sf.net"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

!define SEND_TO_NAME "Record Edit HSQL"                           

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!insertmacro MUI_PAGE_LICENSE "..\General\LICENSE.txt"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Start menu page
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "RecordEdit_HSQL"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page                                                        
;!define MUI_FINISHPAGE_RUN "$JAVA_RUN"  
;!define MUI_FINISHPAGE_RUN_PARAMETERS "-cp $\"$INSTDIR\lib\hsqldbmain.jar$\" org.hsqldb.Server"
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\Docs\hWelcome.htm"
!define RECORDEDIT_JAR "lib\runFullEditor.jar"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
<OutFile default="RecordEdit_Installer_for_HSQL_080.6.exe"/>
InstallDir "$PROGRAMFILES\RecordEdit\HSQL"
ShowInstDetails show
ShowUnInstDetails show

var JAVA_DIR
var JAVA_RUN
var JAVA_RUN1


Section "MainSection" SEC01
  Call GetJRE
  Pop $JAVA_DIR
  StrCpy $JAVA_RUN "$JAVA_DIR\javaw.exe"
  StrCpy $JAVA_RUN1 "$JAVA_DIR\java.exe"
 

  Delete "$INSTDIR\lib\JRecord.jar"
  Delete "$INSTDIR\lib\ZCalendar.jar"
  Delete "$INSTDIR\lib\RecordEdit.jar"
  Delete "$INSTDIR\lib\LayoutEdit.jar"
  Delete "$INSTDIR\lib\cb2xml.Jar"

  Delete "$INSTDIR\lib\StAX.jar"

  <expand overwrite=try outpath="$INSTDIR\License" inpath="..\General" name="LICENSE*.txt">

  <expand overwrite=try outpath="$INSTDIR\lib" inpath="..\Instalation\GeneralDB\lib" name="run*.jar" name1="ZCalendar.jar"  name2="SystemJars.txt">
  ;<expand overwrite=try outpath="$INSTDIR\lib" inpath="..\lib" name="run*.jar"
  ;			name2="JRecord.jar" name3="RecordEdit.jar" name4="LayoutEdit.jar" name5="cb2xml.jar" name6="StAX.jar"/>
  <expand  inpath="..\Instalation\GeneralDB\lib" name="icons*.zip" name1="*.ico" />
  <expand  inpath="..\Instalation\hsqldb\lib\" name="properties.zip" name1="*.txt"/>
  <expand  inpath="..\Instalation\hsqldb_izpack\lib" name="*Edit.pack" name1="cb2xml.pack" name4="chardet.pack"  name5="ZCalendar.pack"/>
  <expand  inpath="..\Instalation\hsqldb_izpack\lib" name="j*.pack"  name1="JRecord.propertie*" name2="RunUnpack.exe" name3="velocity-1.7*.pack"/>
  <psc proc="unix">
    <expand  inpath="..\Instalation\hsqldb_izpack\lib" name="JRecord.pack">
  </psc>
  <psc proc="normal">
    <expand  inpath="..\Instalation\hsqldb_izpack\lib" name="hsqldbmain.pack"/>
  </psc>
  File "NsisUnpack.jar"

   exec '"$JAVA_RUN1" -jar "$INSTDIR\lib\NsisUnpack.jar" $INSTDIR\lib'

  <expand overwrite=try outpath="$INSTDIR\lib\net\sf\RecordEditor\utils" 
                        inpath="..\Instalation\hsqldb\lib\net\sf\RecordEditor\utils\" name="*.properties"/>  
  
                          <expand overwrite="try" outpath="$INSTDIR\Docs" inpath="..\Instalation\hsqldb\Docs" name="h*.htm" name1="RecordEdit.htm" name2="rehMan*.htm"/>
  <expand inpath="..\Instalation\GeneralDB\Docs" name="Hlp*.htm" name1="CobolEditor.htm" name2="Ex*.htm" name3="syntax.css" name4="HowTo.htm"/>
  <expand inpath="..\Instalation\GeneralDB\Docs\"  name2="diff1.html" name3="Copy.htm"/>
  <expand outpath="$INSTDIR\Docs\jsTree" inpath="..\Instalation\GeneralDB\Docs\JSTREE\" name="*.gif" name1="*.css" name2="*.js"/>
  <expand overwrite="try" outpath="$INSTDIR\Docs\Diagram" inpath="..\Instalation\GeneralDB\Docs\Diagram\"  name="*.png" DateCheck=yes/>
 
  <expand outpath="$PROFILE\RecordEditor_HSQL\CopyBook\Cobol" inpath="..\Instalation\GeneralDB\CopyBook\Cobol" name="*.*" DateCheck=yes/>
  <expand outpath="$PROFILE\RecordEditor_HSQL\CopyBook\cb2xml" inpath="..\Instalation\GeneralDB\CopyBook\cb2xml" name="*.xml" DateCheck=yes/>
  <expand outpath="$PROFILE\RecordEditor_HSQL\CopyBook\Csv" inpath="..\Instalation\GeneralDB\CopyBook\Csv" name1="*.Txt" DateCheck=yes/>
  <expand outpath="$PROFILE\RecordEditor_HSQL\CopyBook\Xml" inpath="..\Instalation\GeneralDB\CopyBook\Xml" name1="*.Xml" DateCheck=yes/>
;;  <expand outpath="$INSTDIR\Copybook" inpath="..\Instalation\GeneralDB\Copybook" name="*.txt" DateCheck=yes/>
  <expand overwrite=try outpath="$PROFILE\RecordEditor_HSQL\SampleVelocityTemplates\Copybook" inpath="..\Instalation\GeneralDB\SampleVelocityTemplates\Copybook" name="*.vm"/>
  <expand overwrite=try outpath="$PROFILE\RecordEditor_HSQL\SampleVelocityTemplates\File" inpath="..\Instalation\GeneralDB\SampleVelocityTemplates\File" name="*.vm"/>
  <expand overwrite=try outpath="$PROFILE\RecordEditor_HSQL\SampleFiles" 
                        inpath="..\Instalation\GeneralDB\SampleFiles\" name="Ams_LocDownload_20041228_Extract*.txt"/>  
  <expand overwrite=try inpath="..\SampleFiles" name="*.txt" name1="*.bin" name2="xmlModDTAR020.bin.xml" DateCheck=yes/>  
  <expand overwrite=try inpath="..\SampleFiles" name="*.csv"  DateCheck=yes/>
  <expand overwrite=try outpath="$PROFILE\RecordEditor_HSQL\SampleFiles\Xml" inpath="..\Instalation\GeneralDB\SampleFiles\Xml" name="*.xml"/>  

  <expand overwrite=try outpath="$PROFILE\RecordEditor_HSQL" inpath="..\Instalation\hsqldb_izpack\HSQLDB\" 
  		name1="Files.txt" name="CobolFiles.txt"  name3="UserJars.txt"/>  
  <expand overwrite=off inpath="..\Instalation\hsqldb\RecordEditor_HSQL_nsis\"  name1="Params.Properties" name2="Properties.zip">  
	
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\Copy"          inpath="..\Instalation\GeneralDB\User\Copy"         name="*.xml" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\Compare"       inpath="..\Instalation\GeneralDB\User\Compare"      name="*.xml" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\Filter"        inpath="..\Instalation\GeneralDB\User\Filter"       name="*.xml" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\LayoutExport"  inpath="..\Instalation\GeneralDB\User\LayoutExport" name="*.xml" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\RecordTree"    inpath="..\Instalation\GeneralDB\User\RecordTree"   name="*.xml" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\SortTree"      inpath="..\Instalation\GeneralDB\User\SortTree"     name="*.xml" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\Xslt"          inpath="..\Instalation\GeneralDB\User\Xslt"         name="*.xsl" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\ExportScripts" inpath="..\Instalation\GeneralDB\User\ExportScripts"  name="*.*" />  
  <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\User\Scripts"       inpath="..\Instalation\GeneralDB\User\Scripts"        name="*.*" />  

  <psc proc="normal">
    <expand overwrite=off outpath="$PROFILE\RecordEditor_HSQL\Database" inpath="..\Instalation\hsqldb\Database" name="*"/>
  </psc>

    
  SetOverwrite on
;  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\Record Edit HSQL" 
;  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\Record Edit HSQL\command"

  
;  WriteRegStr HKEY_CLASSES_ROOT "*\Shell\Record Edit HSQL" "" ""
;  WriteRegStr HKEY_CLASSES_ROOT "*\Shell\Record Edit HSQL\command" "" "$\"$JAVA_RUN$\" -cp $\"$INSTDIR\lib\LayoutEdit.jar;$INSTDIR\lib\hsqldbmain.jar$\" net.sf.RecordEditor.edit.FullEditor  $\"%1$\""
  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\${SEND_TO_NAME}\command"
  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\${SEND_TO_NAME}" 

  
  WriteRegStr HKEY_CLASSES_ROOT "*\Shell\${SEND_TO_NAME}" "" ""
  WriteRegStr HKEY_CLASSES_ROOT "*\Shell\${SEND_TO_NAME}\command" "" "$\"$JAVA_RUN$\" -jar $\"$INSTDIR\${RECORDEDIT_JAR}$\" $\"%1$\""


  ClearErrors
  FileOpen $0 $INSTDIR\lib\EditBigFile.Bat w
  IfErrors done
  FileWrite $0 "start /b  javaw  -Xmx700m -jar $\"$INSTDIR\${RECORDEDIT_JAR}$\""
  FileClose $0
  
  FileOpen $0 $INSTDIR\lib\BatchCopy.Bat w
  IfErrors done
  FileWrite $0 "start /b  javaw -jar $\"$INSTDIR\lib\run.jar net.sf.RecordEditor.copy.BatchCopyDbLayout %*$\""
  FileClose $0
  done:

SectionEnd

Section -AdditionalIcons
  SetShellVarContext all
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\CobolEditor.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\Edit RecordEditor Startup Properties.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\Run with Velocity.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\CobolEditor Documentation.lnk"

  Delete "$SMPROGRAMS\$ICONS_GROUP\Basic Editor.lnk"
   Delete "$SMPROGRAMS\$ICONS_GROUP\Full Editor.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Record Editor Manual.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Record Edit.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Record Layout Edit.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Stop Server.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Start Server.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\HowTo.lnk"
 

  SetShellVarContext current
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application

;  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP\Utils"
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP\Documentation"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Full Editor.lnk" "$JAVA_RUN"  "-jar $\"$INSTDIR\${RECORDEDIT_JAR}$\"" "$INSTDIR\lib\RecordEdit.ico"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Record Layout Edit.lnk" "$JAVA_RUN"  "-jar $\"$INSTDIR\lib\runLayouteditor.jar$\"" "$INSTDIR\lib\LayoutEdit.ico"
;  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Documentation\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Documentation\Record Editor Manual.lnk" "$INSTDIR\Docs\hRecordEdit.htm"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Documentation\Examples.lnk" "$INSTDIR\Docs\ExampleFR.htm"  
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Documentation\FileCopy.lnk" "$INSTDIR\Docs\Copy.htm"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Documentation\FileCompare.lnk" "$INSTDIR\Docs\diff1.html"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Documentation\HowTo.lnk" "$INSTDIR\Docs\HowTo.htm"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\Editor Big Files.lnk" "$INSTDIR\lib\EditBigFile.Bat"  "" "$INSTDIR\lib\RecordEdit.ico"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\Edit RecordEditor Startup Properties.lnk" "$JAVA_RUN" "-jar $\"$INSTDIR\lib\run.jar$\" net.sf.RecordEditor.editProperties.EditOptions" "$INSTDIR\lib\Utility.ico"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\Run with Velocity.lnk" "$JAVA_RUN" "-jar $\"$INSTDIR\lib\run.jar$\" net.sf.RecordEditor.edit.util.RunVelocityGui"  "$INSTDIR\lib\Utility.ico"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\CobolEditor.lnk" "$JAVA_RUN" "-jar $\"$INSTDIR\lib\run.jar$\" net.sf.RecordEditor.editFileLayout.Edit"  "$INSTDIR\lib\Cobol.ico"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\CobolEditor Documentation.lnk" "$INSTDIR\Docs\CobolEditor.htm"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\FileCompare.lnk" "$JAVA_RUN" "-jar $\"$INSTDIR\lib\run.jar$\" net.sf.RecordEditor.diff.CompareDBLayout"  "$INSTDIR\lib\Utility.ico"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\FileCopy.lnk" "$JAVA_RUN" "-jar $\"$INSTDIR\lib\run.jar$\" net.sf.RecordEditor.copy.CopyDBLayout"  "$INSTDIR\lib\Utility.ico"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Utils\Uninstall.lnk" "$INSTDIR\uninst.exe"

 
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Stop Server.lnk" "$JAVA_RUN" "-jar $\"$INSTDIR\lib\run.jar$\" net.sf.RecordEditor.layoutEd.ShutdownHSQLDB"  
 ;CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Stop Server.lnk" "$JAVA_RUN"  "-cp $\"$INSTDIR\lib\LayoutEdit.jar;$INSTDIR\lib\hsqldbmain.jar;$INSTDIR\lib\RecordEdit.jar$\" net.sf.RecordEditor.layoutEd.ShutdownHSQLDB" 

  SetOutPath "$PROFILE\RecordEditor_HSQL\Database"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Start Server.lnk" "$JAVA_RUN"  "-cp $\"$INSTDIR\lib\hsqldbmain.jar$\" org.hsqldb.Server" 
  CreateShortCut "$SMSTARTUP\Start HSQL Server.lnk" "$JAVA_RUN"  "-cp $\"$INSTDIR\lib\hsqldbmain.jar$\" org.hsqldb.Server" 


;  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
;  CreateDirectory "$SMPROGRAMS\RecordEdit_HSQL"
;  CreateShortCut "$SMPROGRAMS\RecordEdit_HSQL\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
;  CreateShortCut "$SMPROGRAMS\RecordEdit_HSQL\Uninstall.lnk" "$INSTDIR\uninst.exe"
    !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

Function GetJRE
;
;  Find JRE (Java.exe etc)
;  1 - in .\jre directory (JRE Installed with application)
;  2 - in JAVA_HOME environment variable
;  3 - in the registry
;  4 - assume javaw.exe in current dir or PATH

  Push $R0
  Push $R1

  ClearErrors
  StrCpy $R0 "$EXEDIR\jre\bin\"
  IfFileExists $R0 JreFound
  StrCpy $R0 ""

  ClearErrors
  ReadEnvStr $R0 "JAVA_HOME"
  StrCpy $R0 "$R0\bin\"
  IfErrors 0 JreFound

  ClearErrors
  ReadRegStr $R1 HKLM "SOFTWARE\JavaSoft\Java Runtime Environment" "CurrentVersion"
  ReadRegStr $R0 HKLM "SOFTWARE\JavaSoft\Java Runtime Environment\$R1" "JavaHome"
  StrCpy $R0 "$R0\bin\"

  IfErrors 0 JreFound
  StrCpy $R0 ""

  ClearErrors
  StrCpy $R0 "$PROGRAMFILES\Merant\vm\common\jre\win32\bin\"
  IfFileExists $R0 JreFound

 JreFound:
  Pop $R1
  Exch $R0
FunctionEnd


Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"

  SetShellVarContext current

  <WriteDelete/>
  Delete "$INSTDIR\lib\JRecord.jar"
  Delete "$INSTDIR\lib\velocity-1.7.jar"
  Delete "$INSTDIR\lib\velocity-1.7-dep.jar"
  Delete "$INSTDIR\lib\ZCalendar.jar"
  Delete "$INSTDIR\lib\RecordEdit.jar"
  Delete "$INSTDIR\lib\LayoutEdit.jar"
  Delete "$INSTDIR\lib\cb2xml.Jar"
  Delete "$INSTDIR\lib\hsqldbmain.jar"
  Delete "$INSTDIR\lib\StAX.jar"
  Delete "$INSTDIR\lib\EditBigFile.Bat"
  Delete "$INSTDIR\lib\NsisUnpack.jar"
  Delete "$INSTDIR\lib\chardet.jar"
  Delete "$INSTDIR\lib\jibx-run.jar"
  Delete "$INSTDIR\lib\jlibdiff.jar"

  Delete "$SMPROGRAMS\RecordEdit_HSQL\Uninstall.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Website.lnk"

  Delete "$SMPROGRAMS\RecordEdit_HSQL\utils\CobolEditor.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\utils\Edit RecordEditor Startup Properties.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\utils\Run with Velocity.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\utils\CobolEditor Documentation.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Documentation\Record Editor Manual.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Record Edit.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Record Layout Edit.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Stop Server.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Start Server.lnk"      
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Documentation\Examples.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Full Editor.lnk"
  Delete "$SMPROGRAMS\RecordEdit_HSQL\Documentation\HowTo.lnk"


  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\Record Editor Manual.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Record Edit.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Record Layout Edit.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Stop Server.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Start Server.lnk"      
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\Examples.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Full Editor.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\HowTo.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\Editor Big Files.lnk"                                                               
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\CobolEditor.lnk"                                         
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\Edit RecordEditor Startup Properties.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\Run with Velocity.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\CobolEditor Documentation.lnk"

  Delete "$SMPROGRAMS\$ICONS_GROUP\Basic Editor.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\Examples.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Full Editor.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\Record Editor Manual.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Record Edit.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Record Layout Edit.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Stop Server.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Start Server.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\HowTo.lnk"
  
  Delete "$SMSTARTUP\Start HSQL Server.lnk" 

  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\CobolEditor Documentation.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\FileCompare.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\FileCopy.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\utils\Editor Big Files.lnk" 
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\Examples.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\FileCompare.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\FileCopy.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\HowTo.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Documentation\Record Editor Manual.lnk"


  RMDir "$SMPROGRAMS\$ICONS_GROUP\Documentation"
  RMDir "$SMPROGRAMS\$ICONS_GROUP\Utils"
  RMDir "$SMPROGRAMS\$ICONS_GROUP"
  RMDir "$SMPROGRAMS\RecordEdit_HSQL"

  RMDir "$INSTDIR\Copybook\cb2xml"
  RMDir "$INSTDIR\Copybook\Cobol"
  RMDir "$INSTDIR\Copybook\Csv"
  RMDir "$INSTDIR\Copybook"

  RMDir "$INSTDIR\lib\utils"
  RMDir "$INSTDIR\lib\edit"
  RMDir "$PROFILE\RecordEditor_HSQL\Copybook\cb2xml"
  RMDir "$PROFILE\RecordEditor_HSQL\Copybook\Cobol"
  RMDir "$PROFILE\RecordEditor_HSQL\Copybook\Csv"
  RMDir "$PROFILE\RecordEditor_HSQL\Copybook\Xml"
  RMDir "$PROFILE\RecordEditor_HSQL\Copybook"

  RMDir "$INSTDIR\src"
  RMDir "$INSTDIR\lib\net"
  RMDir "$INSTDIR\lib"
  RMDir "$INSTDIR\Docs\jsTree"
  RMDir "$INSTDIR\Docs\Diagram"
  RMDir "$INSTDIR\Docs"
  RMDir "$INSTDIR\License"
  RMDir "$PROFILE\RecordEditor_HSQL\SampleVelocityTemplates\Copybook"
  RMDir "$PROFILE\RecordEditor_HSQL\SampleVelocityTemplates\File"
  RMDir "$PROFILE\RecordEditor_HSQL\SampleVelocityTemplates"
  RMDir "$PROFILE\RecordEditor_HSQL\SampleFiles\xml"
  RMDir "$PROFILE\RecordEditor_HSQL\SampleFiles"
  RMDir "$PROFILE\RecordEditor_HSQL\Database"
  RMDir "$PROFILE\RecordEditor_HSQL\User\Copy"
  RMDir "$PROFILE\RecordEditor_HSQL\User\Compare"
  RMDir "$PROFILE\RecordEditor_HSQL\User\Filter"
  RMDir "$PROFILE\RecordEditor_HSQL\User\RecordTree"
  RMDir "$PROFILE\RecordEditor_HSQL\User\SortTree"
  RMDir "$PROFILE\RecordEditor_HSQL\User\Xslt"
  RMDir "$PROFILE\RecordEditor_HSQL\User"
  RMDir "$INSTDIR"         
  RMDir "$PROFILE\RecordEditor_HSQL"
  
;  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\Record Edit HSQL" 
;  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\Record Edit HSQL\command"

  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\${SEND_TO_NAME}\command"
  DeleteRegKey HKEY_CLASSES_ROOT "*\Shell\${SEND_TO_NAME}" 
                                                                                       


  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  SetAutoClose true
SectionEnd