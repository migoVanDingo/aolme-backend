-- AOLME DB V2

-- USER TABLE:
CREATE TABLE user( id INT NOT NULL AUTO_INCREMENT, user_id VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, hash VARCHAR(1024) NOT NULL, firstname VARCHAR(255) NULL, lastname VARCHAR(255) NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- USER GROUP TABLE:
CREATE TABLE user_group(id INT NOT NULL AUTO_INCREMENT, user_group_id VARCHAR(255) NOT NULL, user_id VARCHAR(255) NOT NULL, name VARCHAR(255) NULL,  description VARCHAR(512) NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- ORGANIZATION TABLE:
CREATE TABLE organization(id INT NOT NULL AUTO_INCREMENT, organization_id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, email VARCHAR(255) NULL, description VARCHAR(1024) NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- ORG GROUP TABLE:
CREATE TABLE org_group(id INT NOT NULL AUTO_INCREMENT, org_group_id VARCHAR(255), description VARCHAR(255) NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));


-- ENTITY USER TABLE:
CREATE TABLE entity_user( id INT NOT NULL AUTO_INCREMENT, entity_user_id VARCHAR(255) NOT NULL, entity_id 	VARCHAR(255) NOT NULL, user_id VARCHAR(255) NOT NULL, entity_type VARCHAR(255) NOT NULL, status VARCHAR(255) NOT NULL, active_from VARCHAR(255) NULL, active_to VARCHAR(255) NULL, entity_status VARCHAR(255) NOT NULL, roles VARCHAR(255) NOT NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- ENTITY GROUP TABLE:
CREATE TABLE entity_group(id INT NOT NULL AUTO_INCREMENT, entity_group_id VARCHAR(255) NOT NULL, parent_id VARCHAR(255) NULL, name VARCHAR(255) NULL, access VARCHAR(255) NOT NULL, entity_type VARCHAR(64) NOT NULL, active_from VARCHAR(255) NULL, active_to VARCHAR(255) NULL, entity_status VARCHAR(255) NOT NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- ENTITY GROUP MEMBER TABLE:
CREATE TABLE entity_group_member(id INT NOT NULL AUTO_INCREMENT, entity_group_id VARCHAR(255) NOT NULL, entity_id VARCHAR(255) NOT NULL,  active_from VARCHAR(255) NULL, active_to VARCHAR(255) NULL, status VARCHAR(255) NOT NULL, is_primary INT NOT NULL,  is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));



-- PROJECT TABLE:
CREATE TABLE project(id INT NOT NULL AUTO_INCREMENT, project_id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(1024) NULL, owner VARCHAR(255) NOT NULL, ls_project_id VARCHAR(255) NULL, is_public INT NOT NULL, entity_id VARCHAR(255) NOT NULL,  is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- REPOSITORY TABLE:
CREATE TABLE repository(id INT NOT NULL AUTO_INCREMENT, repo_id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(1024) NULL, owner VARCHAR(255) NOT NULL, is_public INT NOT NULL, entity_type VARCHAR(255) NOT NULL, entity_id VARCHAR(255) NOT NULL,  is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- REPO_ITEM TABLE:
CREATE TABLE repo_item(id INT NOT NULL AUTO_INCREMENT, file_id VARCHAR(255) NOT NULL, repo_id VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- FILES TABLE:
CREATE TABLE files(id INT NOT NULL AUTO_INCREMENT, file_id VARCHAR(255) NOT NULL, entity_id VARCHAR(255) NOT NULL, path VARCHAR(512) NOT NULL, name VARCHAR(255) NULL, description VARCHAR(1024) NULL, extension VARCHAR(7) NULL, type VARCHAR(255) NOT NULL,  is_public INT NOT NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- LABEL STUDIO PROJECT INFO:
CREATE TABLE label_studio_project_info(id INT NOT NULL AUTO_INCREMENT, ls_project_id VARCHAR(32) NOT NULL, dataset_id VARCHAR(32) NOT NULL, entity_id VARCHAR(32) NULL, title VARCHAR(255) NULL, description VARCHAR(255) NULL, label_config VARCHAR(255) NULL, expert_instruction VARCHAR(255) NULL, color VARCHAR(255) NULL, model_version VARCHAR(255) NULL, sampling VARCHAR(255) NULL, task_data_login VARCHAR(255) NULL, task_data_password VARCHAR(255) NULL, skip_queue VARCHAR(255) NULL, pinned_at VARCHAR(255) NULL, organization INT NULL, maximum_annotations INT NULL, overlap_cohort_percentage INT NULL, show_instructions INT NULL, show_skip_button INT NULL, enable_empty_annotation INT NULL, show_annotation_history INT NULL, is_published INT NULL, is_draft INT NULL, show_collab_predictions INT NULL, show_ground_truth_first INT NULL, show_overlap_first INT NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

--LABEL STUDIO PROJECT
CREATE TABLE label_studio_project(id INT NOT NULL AUTO_INCREMENT, ls_id VARCHAR(32) NOT NULL, repo_id VARCHAR(32) NOT NULL, entity_id VARCHAR(32) NOT NULL, ls_project_id VARCHAR(32) NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(1024) NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- LABEL STUDIO IMPORT STORAGE  
CREATE TABLE ls_import_storage(id INT NOT NULL AUTO_INCREMENT, path VARCHAR(255) NOT NULL, title VARCHAR(255) NOT NULL, project_id VARCHAR(255) NOT NULL, entity_id VARCHAR(255) NULL, user_id VARCHAR(255) NULL, is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

--CREATE USER 'aolme_db_v2'@'localhost' IDENTIFIED BY 'password';

--grant all privileges on *.* to aolme_db_v2@localhost with grant option;

-- DATASET
CREATE TABLE dataset(id INT NOT NULL AUTO_INCREMENT, dataset_id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(1024) NULL, owner VARCHAR(255) NOT NULL, is_public INT NOT NULL, entity_id VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, path VARCHAR(255) NOT NULL,  is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- MODULE
CREATE TABLE module(id INT NOT NULL AUTO_INCREMENT, module_id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(1024) NULL, owner VARCHAR(255) NOT NULL, is_public INT NOT NULL, entity_id VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, path VARCHAR(255) NOT NULL,  is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));

-- CONFIG
CREATE TABLE config(id INT NOT NULL AUTO_INCREMENT, config_id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(1024) NULL, owner VARCHAR(255) NOT NULL, is_public INT NOT NULL, entity_id VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, path VARCHAR(255) NOT NULL,  is_active INT NOT NULL, created_by VARCHAR(255) NOT NULL, created_at VARCHAR(255) NOT NULL, updated_by VARCHAR(255) NULL, updated_at VARCHAR(255) NULL, deleted_by VARCHAR(255) NULL, deleted_at VARCHAR(255) NULL, PRIMARY KEY(id));