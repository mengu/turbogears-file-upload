# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect, response
from pylons.i18n import ugettext as _, lazy_ugettext as l_

from fileupload.lib.base import BaseController
from tg.controllers import CUSTOM_CONTENT_TYPE
from fileupload.model import DBSession, metadata
from fileupload.controllers.error import ErrorController
from fileupload.model.userfile import UserFile

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the fileupload application.
    
    All the other controllers and WSGI applications should be mounted on this
    controller. For example::
    
        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()
    
    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.
    
    """
    
    error = ErrorController()

    @expose('fileupload.templates.index')
    def index(self):
        current_files = DBSession.query(UserFile).all()
        return dict(current_files=current_files)
        
    @expose()
    def save(self, userfile):
        forbidden_files = [".js", ".htm", ".html", ".mp3"]
        for forbidden_file in forbidden_files:
            if userfile.filename.find(forbidden_file) != -1:
                return redirect("/")
        filecontent = userfile.file.read()
        new_file = UserFile(filename=userfile.filename, filecontent=filecontent)
        DBSession.add(new_file)
        DBSession.flush()
        redirect("/view/"+str(new_file.id))
    
    @expose(content_type=CUSTOM_CONTENT_TYPE)
    def view(self, fileid):
        try:
            userfile = DBSession.query(UserFile).filter_by(id=fileid).one()
        except:
            redirect("/")
        content_types = {
            'display': {'.png': 'image/jpeg', '.jpeg':'image/jpeg', '.jpg':'image/jpeg', '.gif':'image/jpeg', '.txt': 'text/plain'},
            'download': {'.pdf':'application/pdf', '.zip':'application/zip', '.rar':'application/x-rar-compressed'}
        }
        for file_type in content_types['display']:
            if userfile.filename.endswith(file_type):
                response.headers["Content-Type"] = content_types['display'][file_type]
        for file_type in content_types['download']:
            if userfile.filename.endswith(file_type):
                response.headers["Content-Type"] = content_types['download'][file_type]
                response.headers["Content-Disposition"] = 'attachment; filename="'+userfile.filename+'"'
        if userfile.filename.find(".") == -1:
            response.headers["Content-Type"] = "text/plain"
        return userfile.filecontent
    
    @expose()
    def delete(self, fileid):
        try:
            userfile = DBSession.query(UserFile).filter_by(id=fileid).one()
        except:
            return redirect("/")
        DBSession.delete(userfile)
        return redirect("/")


