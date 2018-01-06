#!/usr/bin/env python

import requests
import base64
import datetime
import time

# -------------------------------------------------
# Author: Jhonathan Davi A.K.A jh00nbr
# About-me: http://jhonathandavi.com.br
# Blog: lab.insightsecurity.com.br
# Github: github.com/jh00nbr
# Linkedin: https://www.linkedin.com/in/jhonathandavi/
# Twitter @jh00nbr
# -------------------------------------------------

# Change the ADVFN user and password.

__author__ = "Jhonathan Davi A.K.A jh00nbr"
__email__ = "jdavi@insightsecurity.com.br"
__version__ = '0.1'

stocks_bov = ['IBOV11','VALE3','ITUB4','PETR4','GGBR4','USIM5','BBDC4','BBAS3','KROT3','ABEV3','BOVA11','BRAP4','GOAU4','ITSA4','EMBR3','CSNA3','BVMF3','LAME4','PETR3','MGLU3','RADL3','FIBR3','EQTL3','BRML3','CCRO3','LREN3','BRFS3','BPAC11','VIVT4','UGPA3','RAIL3','BRKM5','ESTC3','QUAL3','BBSE3','HYPE3','CIEL3','CSAN3','SUZB3','MRVE3','SMLS3','VVAR11','CMIG4','FLRY3','ELET3','JBSS3','SANB11','RENT3','CVCB3','PCAR4','EGIE3','MULT3','BBDC3','BOVV11','TIMP3','ECOR3','IRBR3','NATU3','TAEE11','ARZZ3','WEGE3','CYRE3','ENBR3','TRPL4','BTOW3','IGTA3','GOLL4','LINX3','KLBN11','ELPL3','VULC3','SBSP3','GFSA3','AZUL4','HGTX3','TIET11','SEER3','ELET6','VLID3','ALPA4','CPLE6','FESA4','CRFB3','TGMA3','ODPV3','CAML3','ALUP11','SLCE3','POMO4','MDIA3','MYPK3','MOVI3','SAPR11','BRSR6','DTEX3','LEVE3','GUAR3','CSMG3','IVVB11','MRFG3','AMAR3','CESP6','QGEP3','MPLU3','TUPY3','ENGI11','SMTO3','RAPT4','EZTC3','WIZS3','PSSA3','CPFE3','GRND3','CGAS5','TOTS3','CMIG3','PRIO3','ITUB3','ANIM3','LAME3','OIBR3','PARD3','SULA11','BEEF3','MEAL3','ABCB4','ALSC3','OIBR4','PIBB11','SAPR4','LIGT3','CZLT33','TEND3','GBIO33','AALR3','LCAM3','HBOR3','DOVL11B','BRPR3','EVEN3','BZLI11','PTBL3','OMGE3','BRIN3','BBPO11','KNRI11','BRAP3','BRCR11','UNIP6','DIRR3','ENEV3','LPSB3','HGBS11','PMAM3','GGRC11','ETER3','CARD3','KNCR11','STBP3','TCSA3','BBRK3','BCFF11','VISC11','JSLG3','JHSF3','MAGG3','SHOW3','TPIS3','ROMI3','JSRE11','GWIR11','GGBR3','SMAL11','ITSA3','MILS3','SSBR3','RDNI3','XPML11','PPLA11','CGRA4','TECN3','POMO3','HGLG11','HGRE11','RLOG3','SAAG11','COCE5','GUAR4','CMCS34','AGRO3','SGPS3','HTMX11','BRIV4','COTY34','VIVT3','LOGN3','CRPG5','EUCA4','POSI3','NFLX34','MLFT4','RSID3','SLED4','BPAN4','FJTA4','VLOL11','MSFT34','CEPE5','FFCI11','AGCX11','DMMO3','PFRM3','KLBN4','ABCP11','CTNM4','SANB4','MALL11','WSON33','PDGR3','MXRF11','FIGS11','SPTW11','IDNT3','LLIS3','CPLE3','FVBI11','RNEW11','PQDP11','FIIB11','DAGB33','CLSC4','BPFF11','SNSL3','DIVO11','MTSA4','FRAS3','AMZO34','GPIV33','UCAS3','SHUL4','BBFI11B','METB34','SHPH11','CPTS11B','GOAU3','MFII11','USIM3','FMXB34','COWC34','PNVL3','AEFI11','KNIP11','GOGL34','ITLC34','TIFF34','FAED11','VRTA11','KEPL3','TRIS3','ALZR11','BOBR4','ATOM3','ALMI11','SAPR3','CGAS3','GRLV11','TRXL11','FAMB11B','TCNO4','FBOK34','TIET4','SCAR3','AAPL34','CEOC11','XPCM11','UNIP3','TBOF11','BERK34','LUPA3','THRA11','BOEI34','SBUB34','FCFL11','DHER34','ANDV34','TRPN3','RNGO11','REDE3','HGCR11','CTKA4','BOAC34','PEPB34','BBVJ11','EDGA11','MSCD34','HONB34','EXXO34','MMXM3','GOGL35','RCSL4','EALT4','JNJB34','TESA3','ECOO11','SANB3','HGJH11','TELB4','JRDM11','MOAR3','OFSA3','VISA34','WALM34','RBRD11','VVAR4','HAGA4','LMTB34','CHVX34','CTXT11','SPRN34','TSLA34','WFCO34','RNDP11','KLBN3','ATTB34','CTGP34','ABBV34','RNEW4','SEDU3','GSHP3','HOME34','NSLU11','BRKM3','BCIA11','BSEV3','PGCO34','JPMC34','BBRC11','CESP3','GILD34','VVAR3','PFIZ34','FDXB34','CPRE3','FOFT11','BEES3','RNEW3','ORCL34','OGXP3','BIIB34','BBSD11','DISB34','TCNO3','FEXC11','CNES11','FHER3','GDBR34','PRML3','CRPG6','BCRI11','TGTB34','ESTR4','FDMO34','RBBV11','FJTA3','BMYB34','BMEB4','AETB34','TWXB34','CEBR6','CCXC3','AIGB34','UNIP5','AMGN34','PINE4','FRIO3','VIVR3','GMCO34','BLAK34','MRCK34','TIET3','RBRF11','DEAI34','FIND11','BRAX11','ROST34','BPHA3','KNRE11','MSBR34','IBMB34','CATP34','CSCO34','KHCB34','ACNB34','GSGI34','ESRX34','UBSG34','BGIP4','CVSH34','COLG34','CTSH34','SLBG34','VLOE34','CEEB3','COCA34','UPAC34','CGRA3','TRVC34','QCOM34','JBDU4','UTEC34','UBSR11','MCDC34','GEOO34','MDLZ34','COPH34','RAPT3','NIKE34','MDTC34','BAUH4','KMBB34','MMMC34','FIIP11B','CXTL11','IDVL4','PTNT4','MBRF11','CCPR3','TEXA34','CLGN34','SSFO34','PNVL4','VERZ34','MSPA3','AXPB34','PORD11','FCXO34','MGEL4','ATSA11B','FLMA11','CTAX3','SDIL11','BDLL4','BRIV3','TRNT11','CXRI11','GEPA4','PLRI11','LILY34','ISUS11','ALPA3','DUKB34','CRDE3','FIXX11','CBOP11','OUJP11','RANI3','BAHI3','BMLC11B','BBYY34','XBOV11','ELEK4','MATB11','RBVO11','TKNO4','SNSY5','BRSR3','PATI4','XRXB34','ABTT34','CRIV4','EBAY34','RPMG3','CTSA3','LIXC3','CLSC3','USBC34','BONY34','CSAB3','LIXC4','TRPL3','AALL34','RBGS11','CSAB4','ARMT34','SCHW34','HALI34','EEEL3','BTTL4','TMOS34','EEEL4','RBCB11','RPAD6','ONEF11','TWTR34','WHRL4','TOYB4','CTNM3','CORR4','COCE3','CEBR5','CXCE11B','HPQB34','RPAD3','NAFG3','XTED11','ADHM3','ALUP4','BMEB3','WUNI34','TFOF11','USSX34','PEAB3','GEPA3','INEP4','BNBR3','FSLR34','FPAB11','SCPF11','OSXB3','GPSI34','WLMM4','UPSS34','MLFT3','RBDS11','ALUP3','EKTR4','USIM6','CAMB4','FLRP11','MOSC34','HCRI11','MACY34','MSPA4','MAXR11','NUTR3','SULA4','BPAC5','BAZA3','HSHY34','PRSV11','BRGE11','TAEE4','MNDL3','EMAE4','BIOM3','BTTL3','DOMC11','JCPC34','FVPQ11','LIPR3','BEES4','EURO11','HAGA3','MERC4','GPCP3','BRGE12','RDES11','MWET4','BMIN4','LBRN34','MTIG4','HBTS5','CRPG3','WLMM3','JBDU3','PEAB4','BGIP3','TELB3','JFEN3','BMIN3','GOVE11','BPAC3','RSUL4','WPLZ11B','TEKA4','AVON34','ECPR3','CEED3','ENGI3','DASA3','PLAS3','HOOT4','CBEE3','BALM4','CEBR3','RANI4','JOPA4','JOPA3','FESA3','PATI3','WHRL3','BRSR5','BSAN33','CTSA4','ANCR11B','TXRX4','CESP5','FMOF11','SPRI3','CSRN3','SOND5','CREM3','ITEC3','TAEE3','SOND6','AFLT3','ELEK3','CEDO4','MNPR3','PABY11','ODER4','TGAR11B','FBMC4','CARE11','CEDO3','RPAD5','CELP5','BMKS3','TOYB3','ENGI4','HETA4','BNFS11','BRGE3','MAPT4','EUCA3','DTCY3','BRGE6','IDVL3','SULA3','DOHL4','INEP3','CELP3','EDFO11B','AELP3','SLED3','CTKA3','FRTA3','DRIT11B','MEND5','MEND6','CRIV3','RCSL3','AZEV4','CELP7','IGBR3','FIVN11'] 

def load_useragents():
    uas = []
    with open("user-agents.txt", 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[0:-1-0])
    random.shuffle(uas)
return uas

def get_magic_cookies():
	__urls__ = {'url_login':'https://secure.advfn.com/login/secure' }
	
	payload = {'redirect_url': base64.b64encode('https://br.advfn.com'), 'site':'br', 'login_username':'', 'login_password':''}
	headers = {'User-Agent': random.choice(load_useragents())}

	_req = requests.post(__urls__['url_login'], data=payload, headers=headers)

	account_login =  _req.history[0].headers['location']
	req_gsv = requests.get(account_login) # Request for get SID values in content
	cookies_l = req_gsv.history[0].cookies

	if req_gsv.history:
		SID_USER = req_gsv.history[0].cookies['SID']
		USER_COOKIES = [_ for _ in req_gsv.history[0].cookies]
		USER_REQUEST = payload['login_username']

	return cookies_l

def main():
	stocks_failed = []
	stocks_timeout =[]
	date = datetime.datetime.today()

	for stock in stocks_bov:
		req_itd = requests.get('https://br.advfn.com/p.php?pid=data&daily=0&columnheads=1&symbol={0}^{1}'.format('BOV',stock), cookies=get_magic_cookies())
		
		if "There were no results for your query" in req_itd.content:
			print "[ {0} ] Stock Failed\n".format(stock)
			stocks_failed.append(stock)
		elif "You have made too many requests. Please wait before trying to download again." in req_itd.content:
			print "[ {0} ] Stock timeout".format(stock)
			stocks_timeout.append(stock)
			time.sleep(60) #Time of 60 secounds
			pass
		else:	
			print "[ {0} ] Intraday stock :)\n".format(stock)
			with open("csv/INTRADAY_{0}_{1}_{2}-{3}.csv".format('BOV',stock, date.day, date.month), "a") as itd:
				itd.write(req_itd.content)
			itd.close()

if __name__ == '__main__':
	main()
