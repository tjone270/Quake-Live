# branding.py, a plugin for minqlx to brand your server.
# created by Thomas Jones on 06-11-15
# thomas@tomtecsolutions.com

import minqlx

class branding(minqlx.Plugin):
    def __init__(self):
        self.add_hook("new_game", self.brand_map)
        self.set_cvar_once("qlx_serverBrandName", "Branding isn't set up!")
        self.set_cvar_once("qlx_serverBrandTopField", "Set these cvars: 'qlx_serverBrandName', 'qlx_serverBrandTopField', 'qlx_serverBrandBottomField'.")
        self.set_cvar_once("qlx_serverBrandBottomField", "Tip: ^1C^2o^3l^4o^5u^6r ^1v^2a^3l^4u^5e^6s ^1a^2r^3e ^1s^2u^3p^4p^5o^6r^1t^2e^3d^4.")
         
    def brand_map(self):
        minqlx.set_configstring(3, (self.get_cvar("qlx_serverBrandName")))
        minqlx.set_configstring(678, (self.get_cvar("qlx_serverBrandTopField")))
        minqlx.set_configstring(679, (self.get_cvar("qlx_serverBrandBottomField")))
