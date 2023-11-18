from model.project import Project
import random


def test_delete_project(app):
    # app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="newproject"))
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(Project(name=project.name))
    # new_projects = app.project.get_project_list()
    new_projects = app.soap.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.sorted_name) == sorted(new_projects, key=Project.sorted_name)
