from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    # app.session.login("administrator", "root")
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_project_list()
    project = Project(name=random_string("project_name: ", 10))
    app.project.create_project(project)
    # new_projects = app.project.get_project_list()
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.sorted_name) == sorted(new_projects, key=Project.sorted_name)
