fs = require('fs');
var config = {};
config.account = {};
config.verbosityLevel = 1;
config.userAgent = 'NeyBots.ga//CellCraft-Version+V2.1';
config.feederServer = "ws://127.250.0.1:8081";
config.serverPort = 8081;
config.client_uuid = "NEYB";
config.proxies = "proxy.txt";
config.botsPerIp = 1;
config.onboardingTimer = 0;
config.maxBots = 1000;
config.useRandomSkinName = false;
config.useStaticName = "NeyBots.ga";
config.botMode = 'default';
config.minimumMassBeforeFeed = 0;
config.enableSaveMoveTo = true;

config.botSkin = "";
config.botName = "";

GUI = JSON.parse(fs.readFileSync('GUI.conf'));
for(key in GUI) config[key] = GUI[key];

module.exports = config;