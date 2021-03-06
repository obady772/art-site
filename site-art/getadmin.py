from alwan import *

from bs4 import BeautifulSoup

from func import _headers, out, Request, rmhttp, add_http

import re, os

import requests, json


def getadmin(website):
    website = add_http(website)

    panels = ["0admin/", "0manager/", "aadmin/", "acceso.php", "access.php", "access/", "account.asp", "account.html",
              "account.php", "accounts.php", "accounts/", "acct_login/", "adm", "adm.asp", "adm.html", "adm.php",
              "adm/", "adm/admloginuser.asp", "adm/admloginuser.php", "adm/index.asp", "adm/index.html",
              "adm/index.php", "adm_auth.asp", "adm_auth.php", "admcp", "admin", "admin-login.asp", "admin-login.html",
              "admin-login.php", "admin.asp", "admin.htm", "admin.html", "admin.php", "admin/", "ADMIN/",
              "admin/account.asp", "admin/account.html", "admin/account.php", "admin/admin-login.asp",
              "admin/admin-login.html", "admin/admin-login.php", "admin/admin.asp", "admin/admin.html",
              "admin/admin.php", "admin/admin_login.asp", "admin/admin_login.html", "admin/admin_login.php",
              "admin/adminLogin.asp", "admin/adminLogin.htm", "admin/adminLogin.html", "admin/adminLogin.php",
              "admin/controlpanel.asp", "admin/controlpanel.htm", "admin/controlpanel.html", "admin/controlpanel.php",
              "admin/cp.asp", "admin/cp.html", "admin/cp.php", "admin/home.asp", "admin/home.html", "admin/home.php",
              "admin/index.asp", "admin/index.html", "admin/index.php", "admin/login.asp", "admin/login.htm",
              "admin/login.html", "ADMIN/login.html", "admin/login.php", "ADMIN/login.php", "admin1.asp", "admin1.htm",
              "admin1.html", "admin1.php", "admin1/", "admin2.asp", "admin2.html", "admin2.php", "admin2/index.asp",
              "admin2/index.php", "admin2/login.asp", "admin2/login.php", "admin4_account/", "admin4_colon/",
              "admin_area.php", "admin_area/", "admin_area/admin.asp", "admin_area/admin.html", "admin_area/admin.php",
              "admin_area/index.asp", "admin_area/index.html", "admin_area/index.php", "admin_area/login.asp",
              "admin_area/login.html", "admin_area/login.php", "admin_login.asp", "admin_login.html", "admin_login.php",
              "adminare", "adminarea/", "adminarea/admin.asp", "adminarea/admin.html", "adminarea/admin.php",
              "adminarea/index.asp", "adminarea/index.html", "adminarea/index.php", "adminarea/login.asp",
              "adminarea/login.html", "adminarea/login.php", "admincontrol.asp", "admincontrol.html",
              "admincontrol.php", "admincontrol/", "admincontrol/login.asp", "admincontrol/login.html",
              "admincontrol/login.php", "admincp", "admincp/", "admincp/index.asp", "admincp/index.html",
              "admincp/login.asp", "admincp/login.php", "administer/", "administr8.asp", "administr8.html",
              "administr8.php", "administr8/", "administrador/", "administratie/", "administration.html",
              "administration.php", "administration/", "administrator.asp", "administrator.html", "administrator.php",
              "administrator.php/", "administrator/", "administrator/account.asp", "administrator/account.html",
              "administrator/account.php", "administrator/index.asp", "administrator/index.html",
              "administrator/index.php", "administrator/login.asp", "administrator/login.html",
              "administrator/login.php", "administratoraccounts/", "administratorlogin.asp", "administratorlogin.php",
              "administratorlogin/", "administrators.php", "administrators/", "administrivia/", "adminitem.php",
              "adminitem/", "adminitems.php", "adminitems/", "adminLogin.asp", "adminLogin.html", "adminlogin.php",
              "adminLogin.php", "adminLogin/", "adminpanel.asp", "adminpanel.html", "adminpanel.php", "adminpanel/",
              "adminpro/", "admins", "admins.asp", "admins.html", "admins.php", "admins/", "adminsite/", "AdminTools/",
              "admloginuser.asp", "admloginuser.php", "admon/", "ADMON/", "affiliate.asp", "affiliate.php", "auth.php",
              "authadmin.php", "authenticate.php", "authentication.php", "authuser.php", "autologin.php", "autologin/",
              "banneradmin/", "bb-admin/", "bb-admin/admin.asp", "bb-admin/admin.html", "bb-admin/admin.php",
              "bb-admin/index.asp", "bb-admin/index.html", "bb-admin/index.php", "bb-admin/login.asp",
              "bb-admin/login.html", "bb-admin/login.php", "bbadmin/", "bigadmin/", "blog/wp-login.php", "blogindex/",
              "cadmins/", "ccms/", "ccms/index.php", "ccms/login.php", "ccp14admin/", "cgi-bin/login",
              "cgi-bin/login.php", "check.php", "checkadmin.php", "checklogin.php", "checkuser.php", "cms/",
              "cmsadmin.php", "cmsadmin/", "configuration/", "configure/", "control.php", "control/", "controlpanel",
              "controlpanel.asp", "controlpanel.html", "controlpanel.php", "controlpanel/", "cp", "cp.asp", "cp.html",
              "cp.php", "cp/", "cpanel", "cpanel/", "cPanel/", "cpanel_file/", "customer_login/",
              "Database_Administration/", "database_administration/", "ddx/", "ddx/index", "dir-login/", "directadmin/",
              "dotAdmin/", "ezsqliteadmin/", "fileadmin.asp", "fileadmin.html", "fileadmin.php", "fileadmin/",
              "formslogin/", "globes_admin/", "home.asp", "home.html", "home.php", "hpwebjetadmin/", "Indy_admin/",
              "instadmin/", "irc-macadmin/", "isadmin.php", "kpanel/", "letmein.php", "letmein/", "LiveUser_Admin/",
              "log-in.php", "log-in/", "log_in.php", "log_in/", "login", "login-redirect/", "login-us/", "login.asp",
              "login.htm", "login.html", "login.php", "login/", "login1", "login1.php", "login1/", "login_admin",
              "login_admin.php", "login_admin/", "login_db/", "login_out", "login_out.php", "login_out/", "login_user",
              "login_user.php", "loginerror/", "loginflat/", "loginok/", "loginsave/", "loginsuper", "loginsuper.php",
              "loginsuper/", "logo_sysadmin/", "logout", "logout.php", "logout/", "Lotus_Domino_Admin/", "macadmin/",
              "maintenance/", "manage.php", "manage/", "management.php", "management/", "manager.php", "manager/",
              "manuallogin/", "member.php", "member/", "memberadmin.asp", "memberadmin.php", "memberadmin/",
              "members.php", "members/", "memlogin/", "meta_login/", "modcp", "modcp/", "modelsearch/admin.asp",
              "modelsearch/admin.html", "modelsearch/admin.php", "modelsearch/index.asp", "modelsearch/index.html",
              "modelsearch/index.php", "modelsearch/login.asp", "modelsearch/login.html", "modelsearch/login.php",
              "moderator.asp", "moderator.html", "moderator.php", "moderator.php/", "moderator/", "moderator/admin.",
              "moderator/admin.asp", "moderator/admin.html", "moderator/admin.php", "moderator/login.asp",
              "moderator/login.html", "moderator/login.php", "moderatorcp", "modules/admin/", "myadmin/",
              "navSiteAdmin/", "newsadmin/", "nsw/admin/login.php", "openvpnadmin/", "pages/admin/",
              "pages/admin/admin-login.asp", "pages/admin/admin-login.html", "pages/admin/admin-login.php",
              "panel-administracion/", "panel-administracion/admin.asp", "panel-administracion/admin.html",
              "panel-administracion/admin.php", "panel-administracion/index.asp", "panel-administracion/index.html",
              "panel-administracion/index.php", "panel-administracion/login.asp", "panel-administracion/login.html",
              "panel-administracion/login.php", "panel.php", "panel/", "panelc/", "paneldecontrol/", "pgadmin/",
              "phpldapadmin/", "phpMyAdmin", "phpmyadmin/", "phpMyAdmin/themes/", "phppgadmin/", "phpSQLiteAdmin/",
              "platz_login/", "power_user/", "processlogin.php", "project-admins/", "PSUser/", "pureadmin/",
              "radmind-1/", "radmind/", "rcjakar/admin/login.php", "rcLogin/", "registration/", "relogin.htm",
              "relogin.html", "relogin.php", "root/", "secret/", "secrets/", "secure/", "security/", "Server.asp",
              "Server.html", "Server.php", "Server/", "server/", "server_admin_small/", "ServerAdministrator/",
              "showlogin/", "sign-in.php", "sign-in/", "sign_in.php", "sign_in/", "signin.php", "signin/",
              "simpleLogin/", "siteadmin.php", "siteadmin/", "siteadmin/index.asp", "siteadmin/index.php",
              "siteadmin/login.asp", "siteadmin/login.html", "siteadmin/login.php", "smblogin/", "sql-admin/",
              "ss_vms_admin_sm/", "sshadmin/", "staradmin/", "sub-login/", "super", "Super-Admin/", "super.php",
              "super1", "super1.php", "super1/", "super_index", "super_index.php", "super_login", "super_login.php",
              "superman", "superman.php", "superman/", "supermanager", "supermanager.php", "superuser", "superuser.php",
              "superuser/", "supervise/", "supervise/Login", "supervise/Login.php", "supervisor/", "support_login/",
              "sys-admin/", "sysadm.php", "sysadm/", "sysadmin.asp", "sysadmin.html", "sysadmin.php", "SysAdmin/",
              "sysadmin/", "SysAdmin2/", "sysadmins/", "system-administration/", "system_administration/", "typo3/",
              "ur-admin.", "ur-admin.asp", "ur-admin.html", "ur-admin.php", "ur-admin/", "user.asp", "user.html",
              "user.php", "user/", "user/admin.php", "useradmin/", "userlogin.php", "UserLogin/", "users.php", "users/",
              "users/admin.php", "usr/", "utility_login/", "uvpanel/", "vadmind/", "vmailadmin/", "vorod.php", "vorod/",
              "vorud.php", "vorud/", "webadmin.asp", "webadmin.html", "webadmin.php", "webadmin/", "WebAdmin/",
              "webadmin/admin.asp", "webadmin/admin.html", "webadmin/admin.php", "webadmin/index.asp",
              "webadmin/index.html", "webadmin/index.php", "webadmin/login.asp", "webadmin/login.html",
              "webadmin/login.php", "webmaster.php", "webmaster/", "websvn/", "wizmysqladmin/", "wp-admin/",
              "wp-admin/index.php", "wp-login.php", "wp-login/", "xlogin/", "yonetici.asp", "yonetici.html",
              "yonetici.php", "yonetim.asp", "yonetim.html", "yonetim.php"]

    print("{}{:<92}| {:<50}".format(c, "URL", "STATUS"))

    for _panels in panels:

        if len(_panels) != 0:

            combo = website + "/" + _panels

            try:

                resp = requests.get(combo, timeout=5, headers=_headers, allow_redirects=False).status_code

                if resp == 200:

                    print("{}{:<92}| {:<50}".format(g, combo, resp))



                elif resp == 301:

                    print("{}{:<92}| {:<50}".format(r, combo, "404"))



                elif resp == 500 or resp == 502:

                    print("{}{:<92}| {:<50}".format(c, combo, "404"))



                else:

                    print("{}{:<92}| {:<50}".format(r, combo, "404"))



            except Exception:

                print("{}{:<92}| {:<50}".format(r, combo, "404"))

