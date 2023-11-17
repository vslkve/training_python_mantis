from model.project import Project
from selenium.webdriver.common.by import By
import random
import string
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        #wd.get('http://localhost/mantisbt-1.2.20/manage_proj_page.php')
        wd.get(self.app.base_url + 'manage_proj_page.php')

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        project_list = []
        for row in wd.find_elements(By.CSS_SELECTOR, "tr.row-1"):
            cells = row.find_elements(By.TAG_NAME, "td")
            name = cells[0].text
            project_list.append(Project(name=name))
        for row in wd.find_elements(By.CSS_SELECTOR, "tr.row-2"):
            cells = row.find_elements(By.TAG_NAME, "td")
            name = cells[0].text
            project_list.append(Project(name=name))
        return project_list

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element(By.XPATH, "//input[@type='submit' and @value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()
        wd.find_element(By.LINK_TEXT, "Proceed")
        time.sleep(5)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element(By.LINK_TEXT, "%s" % name).click()
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete Project"]').click()
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete Project"]').click()
