from kchhd_orm import*

def init_user(u_id):
    user = User(u_id, u"uAcID_%s"%u_id, u"uName_%s"%u_id,
                u"uType_%s"%u_id, u"uPwd_%s"%u_id, u"uDept_%s"%u_id)
    return user

def init_interviewinfo(i_id):
    interviewinfo = InterviewInfo(i_id, u"iResult_%s"%i_id, u"iAddr_%s"%i_id,
                i_id, u"iDT_%s"%i_id, u"iDept_%s"%i_id, i_id)
    return interviewinfo

def init_tableversion(t_id):
    tableversion = Tableversion(t_id, t_id, t_id)
    return tableversion

def init_questions(q_id):
    questions = Questions(q_id, u"qDescription_%s"%q_id)
    return questions

def init_intervieweegroup(g_id):
    intervieweegroup = Intervieweegroup(g_id, u"gName_%s"%g_id, u"gDescription_%s"%g_id)
    return intervieweegroup

def init_subtitle(s_id):
    subtitle = Subtitle(s_id, u"sName_%s"%s_id)
    return subtitle

def init_maintitle(m_id):
    maintitle = Maintitle(m_id, u"mName_%s"%m_id)
    return maintitle

def init_resumeinfo(r_id):
    resumeinfo = ResumeInfo(r_id, u"rCardID_%s"%r_id, u"rName_%s"%r_id, u"rSex_%s"%r_id)
    return resumeinfo 