

```yaml
resin:
  path1: '/resin-admin/'
  path2: ''
  vstring: ''
  exppath: 'https://www.exploit-db.com/exploits/27888/ https://www.exploit-db.com/exploits/30038/'
  defcreds: 'admin:admin'

weblogic:
  path1: '/console/login/LoginForm.jsp'
  path2: ''
  vstring: ''
  exppath: 'http://www.polaris-lab.com/index.php/archives/98/ https://github.com/frohoff/ysoserial https://github.com/5up3rc/weblogic_cmd'
  defcreds: 'weblogic:weblogic'

glassfish:
  path1: '401'
  path2: 'port:4848'
  vstring: ''
  exppath: 'exploit/multi/http/glassfish_deployer https://www.exploit-db.com/exploits/39241/'
  defcreds: 'admin:admin'

websphere:
  path1: '/ibm/console/logon.jsp'
  path2: '/ibm/console'
  vstring: ''
  exppath: 'exploit/windows/misc/ibm_websphere_java_deserialize'
  defcreds: 'system:manager,admin'

JBoss jmx-console:
  路径1: '/jmx-console'
  路径2: '/jmx-console/'
  版本: ''
  exp: './exploit/multi/http/jboss_deploymentfilerepository'
  默认密码: 'admin:admin'

Apache Tomcat:
  路径1: '/manager/html'
  路径2: '/manager'
  版本: ''
  exp: './exploits/multi/http/tomcat_mgr_upload.rb'
  默认密码: 'tomcat:tomcat'

Testlink:
  路径1: '/testlink-1.9.3/login.php'
  路径2: '/testlink/login.php'
  版本: ''
  exp: './exploits/multi/http/testlink_upload_exec.rb'
  默认密码: 'admin:admin'

Hudson Jenkins:
  路径1: '/jenkins/login?from=/jenkins/'
  路径2: '/jenkins/'
  版本: ''
  exp: './auxiliary/scanner/http/jenkins_enum.rb, ./exploits/multi/http/jenkins_script_console.rb'
  默认密码: 'admin:admin'

Apache Axis2:
  路径1: '/axis2/axis2-admin'
  路径2: ''
  版本: ''
  exp: 'blank'
  默认密码: 'admin:axis2'

Ektron CMS:
  路径1: '/cms400min/'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/ektron_xslt_exec.rb'
  默认密码: 'admin:admin'

HP Intelligent Management Center:
  路径1: '/imc'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/hp_imc_mibfileupload.rb, ./auxiliary/scanner/http/hp_imc_reportimgservlt_traversal.rb'
  默认密码: 'admin:admin'

Umbraco CMS:
  路径1: '/umbraco/'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/umbraco_upload_aspx.rb'
  默认密码: 'admin:admin'

Easy File Management Web Server:
  路径1: '/vfolder.ghp'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/efs_fmws_userid_bof.rb'
  默认密码: 'admin:admin'

VMware ESXi:
  路径1: '/folder?dcPath=ha-datacenter'
  路径2: '/mob'
  版本: ''
  exp: ''
  默认密码: 'admin:admin'

SAP ConfigServlet:
  路径1: '/ctc/servlet'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/sap_configservlet_exec_noauth.rb, ./auxiliary/admin/sap/sap_configservlet_exec_noauth.rb'
  默认密码: 'admin:admin'

HP SiteScope:
  路径1: '/SiteScope/'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/hp_sitescope_runomagentcommand.rb, ./exploits/multi/http/hp_sitescope_uploadfileshandler.rb, ./exploits/multi/http/hp_sitescope_issuesiebelcmd.rb, ./auxiliary/scanner/http/hp_sitescope_getfileinternal_fileaccess.rb, ./auxiliary/scanner/http/hp_sitescope_getsitescopeconfiguration.rb, ./auxiliary/scanner/http/hp_sitescope_loadfilecontent_fileaccess.rb'
  默认密码: 'admin:admin'

Owl Intranet Engine:
  路径1: '/owl/admin/index.php?userid=1&newuser'
  路径2: '/owl/admin/index.php?userid=1&action=edituser&owluser=1'
  版本: ''
  exp: 'https://www.exploit-db.com/exploits/36456/'
  默认密码: 'admin:admin'

Oracle Endeca Server:
  路径1: '/ws/control'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/oracle_endeca_exec.rb'
  默认密码: 'admin:admin'

HP AutoPass License Server:
  路径1: '/autopass'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/hp_autopass_license_traversal.rb'
  默认密码: 'admin:admin'

Dell SonicWALL (Plixer) Scrutinizer:
  路径1: '/d4d/statusFilter.php'
  路径2: ''
  版本: ''
  exp: './exploits/windows/http/sonicwall_scrutinizer_sqli.rb'
  默认密码: 'admin:admin'

v0pCr3w:
  路径1: '/jos.php'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/v0pcr3w_exec.rb'
  默认密码: 'admin:admin'

Moodle:
  路径1: '/moodle/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/moodle_cmd_exec.rb'
  默认密码: 'admin:admin'

Auxilium RateMyPet:
  路径1: '/Auxiliumpetratepro/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/auxilium_upload_exec.rb'
  默认密码: 'admin:admin'

STUNSHELL:
  路径1: '/IDC.php'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/stunshell_eval.rb'
  默认密码: 'admin:admin'

Sflog CMS:
  路径1: '/sflog/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/sflog_upload_exec.rb'
  默认密码: 'admin:admin'

Apache Struts:
  路径1: '/struts2-blank/example/HelloWorld.action'
  路径2: '/blank-struts2/login.action'
  版本: ''
  exp: './exploits/multi/http/struts_code_exec_classloader.rb, ./exploits/multi/http/struts_code_exec_parameters.rb, ./exploits/multi/http/struts_default_action_mapper.rb'
  默认密码: 'admin:admin'

Apache Struts:
  路径1: '/blank-struts2/login.action'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/struts_code_exec_parameters.rb'
  默认密码: 'admin:admin'

MobileCartly:
  路径1: '/mobilecartly/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/mobilecartly_upload_exec.rb'
  默认密码: 'admin:admin'

MediaWiki:
  路径1: '/mediawiki/index.php?title=Special:UserLogin&returnto=Main_Page'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/mediawiki_thumb.rb'
  默认密码: 'admin:password'

qdPM:
  路径1: '/qdPM/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/qdpm_upload_exec.rb'
  默认密码: 'admin:admin'

WebPageTest:
  路径1: '/gettext.php'
  路径2: '/work/resultimage.php'
  版本: ''
  exp: './exploits/multi/http/webpagetest_upload_exec.rb'
  默认密码: 'admin:admin'

GestioIP:
  路径1: '/gestioip/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/gestioip_exec.rb'
  默认密码: 'admin:admin'

PolarBear CMS:
  路径1: '/polarbearcms'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/polarcms_upload_exec.rb'
  默认密码: 'admin:admin'

JBoss:
  路径1: '/invoker/JMXInvokerServlet'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/jboss_invoke_deploy.rb'
  默认密码: 'admin:admin'

Log1 CMS:
  路径1: '/log1cms2.0/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/log1cms_ajax_create_folder.rb'
  默认密码: 'admin:admin'

WikkaWiki:
  路径1: '/wikka/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/wikka_spam_exec.rb'
  默认密码: 'admin:admin'

CuteFlow:
  路径1: '/cuteflow_v.2.11.2/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/cuteflow_upload_exec.rb'
  默认密码: 'admin:admin'

Apache Roller:
  路径1: '/roller'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/apache_roller_ognl_injection.rb'
  默认密码: 'admin:admin'

PhpTax pfilez:
  路径1: '/phptax/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/phptax_exec.rb'
  默认密码: 'admin:admin'

AjaXplorer:
  路径1: '/AjaXplorer-2.5.5/plugins/access.ssh/checkInstall.php'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/ajaxplorer_checkinstall_exec.rb'
  默认密码: 'admin:admin'

phpMyAdmin:
  路径1: '/phpmyadmin/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/phpmyadmin_preg_replace.rb'
  默认密码: 'admin:admin'

vTiger CRM:
  路径1: '/vtigercrm/index.php?action=index&module=Home'
  路径2: '/vtigercrm/index.php?module=Settings&action=ModuleManager&parenttab=Settings'
  版本: ''
  exp: './exploits/multi/http/vtiger_soap_upload.rb, ./exploits/multi/http/vtiger_php_exec.rb'
  默认密码: 'admin:admin'

eXtplorer:
  路径1: '/com_extplorer_2.1.0/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/extplorer_upload_exec.rb'
  默认密码: 'admin:admin'

Splunk:
  路径1: '/en-US/app/launcher/home'
  路径2: '/en-US/manager/search/apps/local'
  版本: ''
  exp: './exploit/multi/http/splunk_upload_app_exec, http://blog.7elements.co.uk/2012/11/splunk-with-great-power-comes-great-responsibility.html'
  默认密码: 'admin:admin'

FreePBX:
  路径1: '/admin/admin/config.php?type=setup&display=general'
  路径2: '/admin/admin/reports.php'
  版本: ''
  exp: 'https://www.exploit-db.com/search/?description=freepbx'
  默认密码: 'admin:admin'

ManageEngine ServiceDesk Plus:
  路径1: '/WOListView.do'
  路径2: '/admin/admin/reports.php'
  版本: '/SetUpWizard.do?forwardTo=site'
  exp: './exploit/multi/http/manageengine_auth_upload'
  默认密码: 'administrator:administrator'

WhatsUp Gold IPSwitch:
  路径1: '/NmConsole/CoreNm/User/DlgUserLogin/DlgUserLogin.asp'
  路径2: '/NmConsole/Workspace/HomeWorkspace/HomeWorkspace.asp'
  版本: 'Ipswitch WhatsUp Gold premium Edition'
  exp: 'https://www.exploit-db.com/exploits/20035/'
  默认密码: 'admin:admin'

OpenX:
  路径1: '/openx/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/openx_backdoor_php.rb'
  默认密码: 'admin:admin'

Glossword:
  路径1: '/glossword/1.8/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/glossword_upload_exec.rb'
  默认密码: 'admin:admin'

GLPI:
  路径1: '/glpi/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/glpi_install_rce.rb'
  默认密码: 'admin:admin'

Kordil EDMS:
  路径1: '/kordil_edms/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/kordil_edms_upload_exec.rb'
  默认密码: 'admin:admin'

Movable Type:
  路径1: '/mt'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/movabletype_upgrade_exec.rb'
  默认密码: 'admin:admin'

Zabbix:
  路径1: '/zabbix/'
  路径2: '/zabbix/scripts.php'
  版本: ''
  exp: './exploits/multi/http/zabbix_script_exec.rb'
  默认密码: 'admin:admin'

PHP Volunteer Management System:
  路径1: '/bf102/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/php_volunteer_upload_exec.rb'
  默认密码: 'admin:admin'

appRain CMF:
  路径1: '/appRain-q-0.1.5'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/apprain_upload_exec.rb'
  默认密码: 'admin:admin'

Mutiny:
  路径1: '/interface/'
  路径2: ''
  版本: ''
  exp: './exploits/multi/http/mutiny_subnetmask_exec.rb'
  默认密码: 'admin:admin'

Tiki Wiki CMS:
  路径1: '/tiki/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/tikiwiki_unserialize_exec.rb'
  默认密码: 'admin:admin'

Invision Power Board:
  路径1: '/forums/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/invision_pboard_unserialize_exec.rb'
  默认密码: 'admin:admin'

App_Name:
  路径1: '/wordpress'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/wp_property_upload_exec.rb, ./exploits/unix/webapp/wp_asset_manager_upload_exec.rb'
  默认密码: 'admin:admin'

Zimbra Admin:
  路径1: '/zimbraAdmin'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/zimbra_lfi.rb'
  默认密码: 'admin:admin'

Nagios3:
  路径1: '/nagios3/cgi-bin/history.cgi'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/nagios3_history_cgi.rb'
  默认密码: 'admin:admin'

PHP-Charts:
  路径1: '/php-charts_v1.0/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/php_charts_exec.rb'
  默认密码: 'admin:admin'

Open Flash Chart v2:
  路径1: '/php-ofc-library/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/open_flash_chart_upload_exec.rb'
  默认密码: 'admin:admin'

LibrettoCMS File Manager:
  路径1: '/librettoCMS_v.2.2.2/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/libretto_upload_exec.rb'
  默认密码: 'admin:admin'

Horde Framework:
  路径1: '/horde/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/horde_unserialize_exec.rb'
  默认密码: 'admin:admin'

XODA:
  路径1: '/xoda/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/xoda_file_upload.rb'
  默认密码: 'admin:admin'

ZoneMinder Video Server:
  路径1: '/zm/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/zoneminder_packagecontrol_exec.rb'
  默认密码: 'admin:admin'

SePortal:
  路径1: '/seportal'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/seportal_sqli_exec.rb'
  默认密码: 'admin:admin'

WebTester:
  路径1: '/webtester5/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/webtester_exec.rb'
  默认密码: 'admin:admin'

Hastymail:
  路径1: '/hastymail2/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/hastymail_exec.rb'
  默认密码: 'admin:admin'

Joomla:
  路径1: '/joomla'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/joomla_media_upload_exec.rb'
  默认密码: 'admin:admin'

Kimai Time Tracking:
  路径1: '/kimai/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/kimai_sqli.rb'
  默认密码: 'admin:admin'

FlashChat:
  路径1: '/chat/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/flashchat_upload_exec.rb'
  默认密码: 'admin:admin'

Simple E-Document:
  路径1: '/simple_e_document_v_1_31/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/simple_e_document_upload_exec.rb'
  默认密码: 'admin:admin'

EGallery:
  路径1: '/sample'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/egallery_upload_exec.rb'
  默认密码: 'admin:admin'

OpenEMR:
  路径1: '/openemr'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/openemr_upload_exec.rb, ./exploits/unix/webapp/openemr_sqli_privesc_upload.rb'
  默认密码: 'admin:admin'

Basilic:
  路径1: '/basilic-1.5.14/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/basilic_diff_exec.rb'
  默认密码: 'admin:admin'

Narcissus:
  路径1: '/narcissus-master/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/narcissus_backend_exec.rb'
  默认密码: 'admin:admin'

Project Pier:
  路径1: '/pp088/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/projectpier_upload_exec.rb'
  默认密码: 'admin:admin'

OpenSIS:
  路径1: '/opensis/'
  路径2: ''
  版本: ''
  exp: './exploits/unix/webapp/opensis_modname_exec.rb'
  默认密码: 'admin:admin'

V-CMS:
  路径1: '/vcms/'
  路径2: ''
  版本: ''
  exp: './exploits/linux/http/vcms_upload.rb'
  默认密码: 'admin:admin'

Zabbix:
  路径1: '/zabbix'
  路径2: ''
  版本: ''
  exp: './exploits/linux/http/zabbix_sqli.rb'
  默认密码: 'admin:zabbix'

WebCalendar:
  路径1: '/WebCalendar-1.2.4/'
  路径2: ''
  版本: ''
  exp: './exploits/linux/http/webcalendar_settings_exec.rb'
  默认密码: 'admin:admin'

Symantec Web Gateway:
  路径1: '/spywall/pbcontrol.php'
  路径2: ''
  版本: ''
  exp: './exploits/linux/http/symantec_web_gateway_pbcontrol.rb'
  默认密码: 'admin:admin'

WeBid:
  路径1: '/WeBid'
  路径2: ''
  版本: ''
  exp: './exploits/linux/http/webid_converter.rb'
  默认密码: 'admin:admin'

DoliWamp:
  路径1: '/dolibarr/'
  路径2: ''
  版本: ''
  exp: './exploits/linux/http/dolibarr_cmd_exec.rb, ./auxiliary/gather/doliwamp_traversal_creds.rb'
  默认密码: 'admin:admin'

Ruby on Rails Devise:
  路径1: '/users/password'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/http/rails_devise_pass_reset.rb'
  默认密码: 'admin:admin'

Linksys WRT54GL:
  路径1: '/apply.cgi'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/http/linksys_wrt54gl_exec.rb'
  默认密码: 'admin:admin'

JBoss Seam 2:
  路径1: '/seam-booking/home.seam'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/http/jboss_seam_exec.rb'
  默认密码: 'admin:admin'

Plixer Scrutinizer NetFlow:
  路径1: '/cgi-bin/admin.cgi'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/http/scrutinizer_add_user.rb'
  默认密码: 'admin:admin'

Openbravo ERP:
  路径1: '/openbravo/'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/http/openbravo_xxe.rb'
  默认密码: 'admin:admin'

Advantech WebAccess:
  路径1: '/BEMS'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/scada/advantech_webaccess_dbvisitor_sqli.rb'
  默认密码: 'admin:admin'

GE Proficy Cimplicity WebView:
  路径1: '/CimWeb'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/scada/ge_proficy_substitute_traversal.rb'
  默认密码: 'admin:admin'

Cisco Secure ACS:
  路径1: '/PI/services/UCP/'
  路径2: ''
  版本: ''
  exp: './auxiliary/admin/cisco/cisco_secure_acs_bypass.rb'
  默认密码: 'admin:admin'

CouchDB:
  路径1: '/_all_dbs'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/couchdb/couchdb_enum.rb'
  默认密码: 'admin:admin'

SAP SOAP Service:
  路径1: '/sap/bc/soap/rfc'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/sap/sap_soap_rfc_brute_login.rb'
  默认密码: 'admin:admin'

Apache ActiveMQ:
  路径1: '/admin/index.jsp'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/apache_activemq_source_disclosure.rb'
  默认密码: 'admin:admin'

SVN:
  路径1: '/.svn/'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/svn_wcdb_scanner.rb'
  默认密码: 'admin:admin'

Bitweaver:
  路径1: '/bitweaver/'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/bitweaver_overlay_type_traversal.rb'
  默认密码: 'admin:admin'

Dell iDRAC:
  路径1: '/data/login'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/dell_idrac.rb'
  默认密码: 'admin:admin'

JBoss Status Servlet:
  路径1: '/status'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/jboss_status.rb'
  默认密码: 'admin:admin'

OpenMind Message-OS Portal:
  路径1: '/provision/index.php'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/openmind_messageos_login.rb'
  默认密码: 'admin:admin'

ClanSphere:
  路径1: '/clansphere_2011.3/'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/clansphere_traversal.rb'
  默认密码: 'admin:admin'

InfoVista VistaPortal Application:
  路径1: '/VPortal/mgtconsole/CheckPassword.jsp'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/infovista_enum.rb'
  默认密码: 'admin:admin'

Atlassian Crowd:
  路径1: '/crowd/services'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/atlassian_crowd_fileaccess.rb'
  默认密码: 'admin:admin'

S40 CMS:
  路径1: '/s40/'
  路径2: ''
  版本: ''
  exp: './auxiliary/scanner/http/s40_traversal.rb'
  默认密码: 'admin:admin'

MyBB:
  路径1: '/forum'
  路径2: ''
  版本: ''
  exp: './auxiliary/gather/mybb_db_fingerprint.rb'
  默认密码: 'admin:admin'

IBM Lotus Notes:
  路径1: '/userinfo/search'
  路径2: ''
  版本: ''
  exp: './auxiliary/gather/ibm_sametime_enumerate_users.rb'
  默认密码: 'admin:admin'

Apache Rave:
  路径1: '/portal'
  路径2: ''
  版本: ''
  exp: './auxiliary/gather/apache_rave_creds.rb'
  默认密码: 'admin:admin'

Drupal OpenID:
  路径1: '/drupal'
  路径2: ''
  版本: ''
  exp: './auxiliary/gather/drupal_openid_xxe.rb'
  默认密码: 'admin:admin'

Symantec Endpoint Protection Manager:
  路径1: '/servlet/ConsoleServlet'
  路径2: ''
  版本: ''
  exp: '/exploits/windows/http/sepm_auth_bypass_rce'
  默认密码: 'admin:admin'

Panasonic Network Camera WV-SF335:
  路径1: '/live/index.html?Language=0'
  路径2: '/admin/index.html?Language=0'
  版本: ''
  exp: 'Unauthenticate access to LIVE video feed'
  默认密码: 'admin:admin'

AXIS Q7404 Video Encoder:
  路径1: '/view/viewer_index.shtml'
  路径2: '/operator/action_rules.shtml'
  版本: ''
  exp: 'Unauthenticate access to LIVE video feed'
  默认密码: 'admin:admin'

Vivotek Mega-Pixel Network Camera:
  路径1: '/setup/system/system.html'
  路径2: '/media/media_settings.html'
  版本: ''
  exp: 'Unauthenticate access to LIVE video feed'
  默认密码: 'admin:admin'

SVSi N-Command N8002:
  路径1: '/userAdmin.php'
  路径2: ''
  版本: ''
  exp: 'Unauthenticate access to LIVE video feed'
  默认密码: 'admin:admin'

SVSi N-Series 2000 Decoder:
  路径1: '/localplay.php'
  路径2: '/edid.php'
  版本: ''
  exp: 'Unauthenticate access to LIVE video feed'
  默认密码: 'admin:admin'

AlienVault USM:
  路径1: '/ossim/session/login.php'
  路径2: '/ossim/#configuration/administration/users'
  版本: ''
  exp: 'https://www.exploit-db.com/search/?text=alienvault'
  默认密码: 'admin:admin'

Arecont Vision Mega Pixel Panoramic Camera:
  路径1: '/livevideo.html'
  路径2: ''
  版本: 'dinapage'
  exp: 'Unauthenticate access to LIVE video feed'
  默认密码: 'admin:admin'
```