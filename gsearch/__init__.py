import logging
import optparse
import urllib2
import urllib
import simplejson
import gettext
from gettext import gettext as _
gettext.textdomain('gsearch')

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from gsearch import gsearchconfig

class GsearchLens(SingleScopeLens):

	google = "http://google.com"

	class Meta:
		name = 'gsearch'
		description = 'Google search Lens'
		search_hint = 'Search Google'
		icon = 'gsearch.svg'
		search_on_blank=True

	# TODO: Add your categories
	results_category = ListViewCategory("Results", 'dialog-information-symbolic')

	def search(self, search, results):
		# TODO: Add your search results
		for article in self.gsearch_query(search):
 			results.append(article["link"],
					"https://lh3.ggpht.com/-pNnDAecWckI/UCU4tBr6LQI/AAAAAAAACrw/sxVMFBwr2Xc/s1600/Google-Logo.jpg",
					self.results_category,
					"text/html",
					article["title"],
					"Google Search",
					article["link"])
		pass

	def gsearch_query(self, search):
		try:
			#search = search.replace(" ", "|")
			#url = ("https://www.googleapis.com/customsearch/v1?key=AIzaSyBc7-ZaI7z1PDaHRHHLe-zErOpF6RQ0z74&cx=017576662512468239146:omuauf_lfve&q=" + search)
			url = ("http://www.google.com/search?q=" + search)
			results = simplejson.loads(urllib2.urlopen(url).read())
			for element in results["items"]:
				print(element)			
			print "Googling... %s" % (search)
			#return results["items"]
			return results
		except (IOError, KeyError, urllib2.URLError, urllib2.HTTPError, simplejson.JSONDecodeError), err:
			print str(err) + "Error : Unable to Google"
			return []



