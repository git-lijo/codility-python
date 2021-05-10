#from __future__ import division
from scrapy.selector import HtmlXPathSelector
import scrapy
import datetime
from scrapy.contrib.spiders.init import InitSpider
from scrapy import Spider
from scrapy.http import FormRequest
import math
from scrapy.utils.response import open_in_browser
from datetime import *
# http://xplanner.thinkpalm.info:8080/do/edit/time?fkey=690472&returnto=%2Fdo%2Fview%2Ftask%3Foid%3D690433&oid=690433&projectId=70667
# http://xplanner.thinkpalm.info:8080/do/edit/time?fkey=690472&returnto=%2Fdo%2Fview%2Ftask%3Foid%3D693721&oid=693721&projectId=70667
# anj
# http://xplanner.thinkpalm.info:8080/do/edit/time?fkey=690472&returnto=%2Fdo%2Fview%2Ftask%3Foid%3D690431&oid=690431&projectId=70667
xeditpage="http://xplanner.thinkpalm.info:8080/do/edit/time?fkey=690472&returnto=%2Fdo%2Fview%2Ftask%3Foid%3D690433&oid=690433&projectId=70667"
test="http://xplanner.thinkpalm.info:8080/do/edit/time?fkey=690472&returnto=%2Fdo%2Fview%2Ftask%3Foid%3D710012&oid=710012&projectId=70667"
# time=0.0
dd={}
dummy={}
xphome="http://xplanner.thinkpalm.info:8080/do/login"
headuser='itp 1443'
headpass='pass'
xuser='lijo.j'
xpass='Admin@123'
sdate='04/02/2019'
edate='12/02/2019'
date_format = "%d/%m/%Y"
a = datetime.strptime(sdate, date_format)
b = datetime.strptime(edate, date_format)
delta = b - a
noofdays=delta.days + 1
print ('Days = ' + str(delta.days + 1))
np=noofdays/10
lp=noofdays%10
if noofdays%10!=0:
	np=np+1
k=1
class LoginSpider(scrapy.Spider):			#scrapy.Spider
	name='loginspider'
	start_urls=['http://heads.thinkpalm.lan/Default.aspx']
	def parse(self, response):
		VIEWSTATE = response.xpath("//*[@id='__VIEWSTATE']/@value").extract()
		# btnx=response.xpath("//*[@id='btnLogin.x']/@value").extract()
		# btny=response.xpath("//*[@id='btnLogin.y']/@value").extract()
		EV= response.xpath("//*[@id='__EVENTVALIDATION']/@value").extract()
		yield FormRequest.from_response(response,
									formdata={
											'txtUserName': headuser,
											'txtPassword': headpass,
											'__VIEWSTATE': VIEWSTATE,
											'btnLogin.x': '45',
											'btnLogin.y': '14',
											'__EVENTVALIDATION': EV,
											'__VIEWSTATEGENERATOR': 'CA0B0334',
											'ToolkitScriptManager1_HiddenField':';;AjaxControlToolkit,+Version=4.1.60623.0,+Culture=neutral,+PublicKeyToken=28f01b0e84b6d53e:en-GB:187c1d17-2715-476f-9eeb-4fd46e2849ea:f2c8e708:de1feab2:720a52bf:f9cec9bc:589eaa30:a67c2700:ab09e3fe:87104b7c:8613aea7:3202a5a2:be6fb298:f4fab6f6',
											},									
									callback=self.after_login)
	def after_login(self, response):
		# import pdb;pdb.set_trace()
		login=response.css("::text").extract()
		for i in login:
			if 'Welcome' in i:
				print("<<<<======================Successful Login======================>>>>>>>>>>>>>")
		VIEWSTATE = response.xpath("//*[@id='__VIEWSTATE']/@value").extract()
		EVENTVALIDATION = response.xpath("//*[@id='__EVENTVALIDATION']/@value").extract()
		return [FormRequest(url = "http://heads.thinkpalm.lan/Leave/EmployeeSwipeReport.aspx",formdata={'__VIEWSTATE':VIEWSTATE, 
																								'__VIEWSTATEGENERATOR':'8D0E13E6',
																								'__PREVIOUSPAGE':'stKLRmHvDHSWrU7iYiEwPVxhxgvGjIKOk5miJs2w3yesM6KIWGqvzeAcijR8-4JrhUeMW0Vac0n8P4HfqIOzPaKTYyaK559hJEKVsed6kFw1',
																								'__EVENTVALIDATION':EVENTVALIDATION,
																								'ctl00$ContentPlaceHolder1$Module2$DataListModule$ctl10$ImgBtnModule.x':'33',
																								'ctl00$ContentPlaceHolder1$Module2$DataListModule$ctl10$ImgBtnModule.y':'68',
																								'ToolkitScriptManager1_HiddenField':';;AjaxControlToolkit,+Version=4.1.60623.0,+Culture=neutral,+PublicKeyToken=28f01b0e84b6d53e:en-GB:187c1d17-2715-476f-9eeb-4fd46e2849ea:f2c8e708:de1feab2:720a52bf:f9cec9bc:589eaa30:a67c2700:ab09e3fe:87104b7c:8613aea7:3202a5a2:be6fb298',
			},callback = self.parse1)]
	def parse1(self, response):
		sw=response.css("::text").extract()
		for i in sw:
			if 'Swipe History' in i:
				print("<<<======================Inside Swipe Reports=============================>>>")		  
		# import pdb;pdb.set_trace()
		VIEWSTATE = response.xpath("//*[@id='__VIEWSTATE']/@value").extract()
		bx=response.xpath("//*[@id='ctl00$ContentPlaceHolder1$btnShow.x']/@value").extract()
		by=response.xpath('//*[@id="ctl00$ContentPlaceHolder1$btnShow.y"]/@value').extract()
		# import pdb;pdb.set_trace()
		yield FormRequest.from_response(response,
									formdata={
											'__VIEWSTATE': VIEWSTATE,
											'__VIEWSTATEGENERATOR': '2CD25266',
											'__PREVIOUSPAGE':'C7h_BVP0CbOj97mxJTgttgwug_xVQtP-GQigDhIEANic9jMP5vJ5dAC93akS9qFKR02ATces2y-woadXn2fnjwQGu_McI-rTGPgqK2NBVM3ijw8Eu71zHOLSziKGqkWu0',
											'ToolkitScriptManager1_HiddenField':';;AjaxControlToolkit,+Version=4.1.60623.0,+Culture=neutral,+PublicKeyToken=28f01b0e84b6d53e:en-GB:187c1d17-2715-476f-9eeb-4fd46e2849ea:de1feab2:fcf0e993:f2c8e708:720a52bf:f9cec9bc:589eaa30:698129cf:fb9b4c57:ccb96cf9:987bb99b:a4b66312:a67c2700:ab09e3fe:87104b7c:8613aea7:3202a5a2:be6fb298',
											'ctl00$ContentPlaceHolder1$txtFromDate':sdate,
											'ctl00$ContentPlaceHolder1$txtToDate':edate,
											'ctl00$ContentPlaceHolder1$btnShow.x':'31',
											'ctl00$ContentPlaceHolder1$btnShow.y':'4',
											},									
									callback=self.next_page)
	def next_page(self,response):
		global dd,k
		# import pdb;pdb.set_trace()
		if k!=np:
			for i in range(10):
				d1 = str(response.xpath("//*[@id='ContentPlaceHolder1_DailySwipeListView_lblReqDate_" + str(i) + "']/text()").extract_first())
				h1 = str(response.xpath("//*[@id='ContentPlaceHolder1_DailySwipeListView_lblworkedHours_" + str(i) + "']/text()").extract_first())
				if h1!='--:--':
					hr = int(h1.split(':')[0])
					mi=str((float(h1.split(':')[1])/6)/10)
					mi=mi.split('.')[1]
					time=round(float(str(hr)+"."+str(mi)),2)
					if d1 in dd:
						dd[d1]=dd[d1]+time
					else:
						dd[d1]=time
				# else:
				# 	dd[d1]=None
			# import pdb;pdb.set_trace()
			VIEWSTATE = str(response.xpath("//*[@id='__VIEWSTATE']/@value").extract_first())
			argument =  "Page$" + str(k+1)
			k=k+1
			# import pdb;pdb.set_trace()
			yield FormRequest.from_response(response, 
									formdata = {'ToolkitScriptManager1_HiddenField':';;AjaxControlToolkit,+Version=4.1.60623.0,+Culture=neutral,+PublicKeyToken=28f01b0e84b6d53e:en-GB:187c1d17-2715-476f-9eeb-4fd46e2849ea:de1feab2:fcf0e993:f2c8e708:720a52bf:f9cec9bc:589eaa30:698129cf:fb9b4c57:ccb96cf9:987bb99b:a4b66312:a67c2700:ab09e3fe:87104b7c:8613aea7:3202a5a2:be6fb298',
										'__EVENTTARGET':'ctl00$ContentPlaceHolder1$DailySwipeListView',
										'__EVENTARGUMENT': argument,
										'__VIEWSTATE': VIEWSTATE,
										'__VIEWSTATEGENERATOR':'2CD25266',
										'__PREVIOUSPAGE':'C7h_BVP0CbOj97mxJTgttgwug_xVQtP-GQigDhIEANic9jMP5vJ5dAC93akS9qFKR02ATces2y-woadXn2fnjwQGu_McI-rTGPgqK2NBVM3ijw8Eu71zHOLSziKGqkWu0',
										'ctl00$ContentPlaceHolder1$txtFromDate': sdate,
										'ctl00$ContentPlaceHolder1$txtToDate': edate,
										}, 
										callback = self.next_page)
				# for key in sorted(dd):print "%s %s" % (key, dd[key])
				# import pdb;pdb.set_trace()
		elif k==np:
			# import pdb;pdb.set_trace()
			for i in range(lp):
				d1 = str(response.xpath("//*[@id='ContentPlaceHolder1_DailySwipeListView_lblReqDate_" + str(i) + "']/text()").extract_first())
				h1 = str(response.xpath("//*[@id='ContentPlaceHolder1_DailySwipeListView_lblworkedHours_" + str(i) + "']/text()").extract_first())
				if h1!='--:--':
					hr = int(h1.split(':')[0])
					mi=str((float(h1.split(':')[1])/6)/10)
					mi=mi.split('.')[1]
					time=round(float(str(hr)+"."+str(mi)),2)
					if d1 in dd:
						dd[d1]=dd[d1]+time
					else:
						dd[d1]=time

			for key in sorted(dd):print( "%s %s" % (key, dd[key]))
			yield scrapy.Request(xphome,callback=self.xplanhome)
	def xplanhome(self,response):
		# import pdb;pdb.set_trace()
		print ('Xplanner Home')
		return [FormRequest(url = "http://xplanner.thinkpalm.info:8080/do/login",formdata={'userId': xuser,
																							'password': xpass,
																							'action':'Login',
						},callback = self.xplanlog)]
	def xplanlog(self,response):
		# import pdb;pdb.set_trace()
		xp=response.css("::text").extract()
		for i in xp:
			if 'TP-Training' in i:
				print("<<<<====================Successful Xplanner Login================>>>>>>>>>>>>>")
		# import pdb;pdb.set_trace()
		return [FormRequest(url =test,callback=self.edittime)]
	def edittime(self,response):
		# import pdb;pdb.set_trace()
		global dd,dummy
		print ('Edit Time')
		for key in sorted(dd):
			if key not in dummy:
				df= datetime.strptime(key, "%d/%m/%Y").strftime("%Y-%m-%d")		#dateformat
				rh=str(response.xpath("//*[@name='remainingHours']/@value").extract_first())
				f={}
				# import pdb;pdb.set_trace()
				rc=	str(response.xpath("//*[@name='rowcount']/@value").extract_first())				#rowcount
				rc=(int(rc))-1
				for i in range(0,rc):
					e="entryId["+str(i)+"]"															#entryId[]
					# eid.append(str(response.xpath("//*[@name='"+ e +"']/@value").extract_first()))
					f[e]=str(response.xpath("//*[@name='"+ e +"']/@value").extract_first())				
				pr=response.xpath("//*[@selected='selected']/@value").extract()
				pr=[x.encode('UTF8') for x in pr]
				for i in range(0,rc):
					p1="person1Id["+str(i)+"]"																			#person1Id[]
					f[p1]=pr[i*2]
					#str(response.xpath("//*[@selected='selected']/@value")[i].extract())																												
					p2="person2Id["+str(i)+"]"																			#person2Id[]
					f[p2]=pr[(i*2)+1]
					# str(response.xpath("//*[@selected='selected']/@value")[i+1].extract())
				for i in range(0,rc):
					repo="reportDate["+str(i)+"]"
					dv="duration["+str(i)+"]"
					# rdate.append(str(response.xpath("//*[@name='"+ repo +"']/@value").extract_first()))		#reportDate[]
					f[repo]=str(response.xpath("//*[@name='"+ repo +"']/@value").extract_first())
					# dur.append(str(response.xpath("//*[@name='"+ dv +"']/@value").extract_first()))			#duration[]
					f[dv]=str(response.xpath("//*[@name='"+ dv +"']/@value").extract_first())

				f['oid']=str(response.xpath("//*[@name='oid']/@value").extract_first())						#oid
				f['returnto']=str(response.xpath("//*[@name='returnto']/@value").extract_first())				#returnto
				f['fkey']=str(response.xpath("//*[@name='fkey']/@value").extract_first())						#fkey
				f['taskId']=str(response.xpath("//*[@name='taskId']/@value").extract_first())					#taskId
				#convert to str
				er="emptyRow["+str(rc)+"]"
				f[er]=str(response.xpath("//*[@name='"+ er +"']/@value").extract_first())				#emptyRow[rc-1]
				f['action']=str(response.xpath("//*[@name='action']/@value")[0].extract())				#action
				f['submit']=str(response.xpath("//*[@name='submit']/@value").extract_first())					#submit
				#new values to be updated
				# import pdb;pdb.set_trace()
				repo="reportDate["+str(rc)+"]"
				dv="duration["+str(rc)+"]"
				f[repo]=df						#=======
				f[dv]=str(dd[key])							#========
				p1="person1Id["+str(rc)+"]"
				f[p1]=pr[rc*2]
				p2="person2Id["+str(rc)+"]"
				f[p2]=pr[(rc*2)+1]
				e="entryId["+str(rc)+"]"
				f[e]='0'
				rc=rc+1
				f['rowcount']=str(rc)							#========
				f['remainingHours']=rh
				dummy[key]=dd[key]
				# print f
				# for key, value in f.items():
				# 	print("{} {}".format(key, value))
				# for key in sorted(f):
				# 	print "%s %s" % (key, f[key])
				# import pdb;pdb.set_trace()
				return [FormRequest(url ="http://xplanner.thinkpalm.info:8080/do/edit/time",
											formdata=f,	
											dont_filter = True,								
											callback=self.closeiterations)]
		if dummy==dd:
			print ('Equal & Complete------------------------------------------------------')
	def closeiterations(self,response):
		# import pdb;pdb.set_trace()
		o=str(response.xpath("//*[@type='hidden']/@value")[1].extract())
		try:
			print('Close Iterations')
			o=str(response.xpath("//*[@type='hidden']/@value")[1].extract())
			f=str(response.xpath("//*[@type='hidden']/@value")[2].extract())
			r=str(response.xpath("//*[@type='hidden']/@value")[3].extract())
			op=str(response.xpath("//*[@type='hidden']/@value")[4].extract())
			it=str(response.xpath("//*[@type='hidden']/@value")[5].extract())
			st=str(response.xpath("//*[@type='hidden']/@value")[6].extract())
			# import pdb;pdb.set_trace()
			return [FormRequest(url="http://xplanner.thinkpalm.info:8080/do/start/iteration",
									formdata={'oid':o,
												'fkey':	f,
												'returnto': r,
												'operation':op,
												'iterationStartConfirmed':it,
												'saveTime': st,
												'closeIterations':'on',
												'start':'Ok',	
											},
											dont_filter = True,
											callback=self.updatet)]
		except:
			# import pdb;pdb.set_trace()
			print ('Updated-')
			return [FormRequest(url ="http://xplanner.thinkpalm.info:8080/do/view/task",
									formdata={'errorInEdit':'0',
											'oid':o,
											'cutOffDay':'7'
											},
											dont_filter = True,									
									callback=self.added)] 		
	def updatet(self,response):
		# import pdb;pdb.set_trace()
		print ('Updated+')
		o=str(response.xpath("//*[@type='hidden']/@value")[1].extract())
		return [FormRequest(url ="http://xplanner.thinkpalm.info:8080/do/view/task",
									formdata={'errorInEdit':'0',
											'oid':o,
											'cutOffDay':'7'
											},	
									dont_filter = True,								
									callback=self.added)]   	
	def added(self,response):
		# import pdb;pdb.set_trace() 
		print ('Added')
		return [FormRequest(url =test,dont_filter = True,callback=self.edittime)]