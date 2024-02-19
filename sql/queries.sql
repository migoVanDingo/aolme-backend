SELECT
    ri.repo_item_id,
    ri.type
    CASE
        WHEN ri.type = 'DATASET' THEN ds.dataset_id
        WHEN ri.type = 'CONFIG' THEN cf.config_id
        WHEN ri.type = 'MODULE' THEN mo.module_id
        ELSE NULL
    END AS ref_id,
    CASE
        WHEN ri.type = 'DATASET' THEN ds.name
        WHEN ri.type = 'CONFIG' THEN cf.name
        WHEN ri.type = 'MODULE' THEN mo.name
        ELSE NULL
    END AS file_name,
    CASE
        WHEN ri.type = 'DATASET' THEN ds.path
        WHEN ri.type = 'CONFIG' THEN cf.path
        WHEN ri.type = 'MODULE' THEN mo.path
        ELSE NULL
    END AS file_path
    CASE
        WHEN ri.type = 'DATASET' THEN ds.description
        WHEN ri.type = 'CONFIG' THEN cf.description
        WHEN ri.type = 'MODULE' THEN mo.description
        ELSE NULL
    END AS description
    CASE
        WHEN ri.type = 'DATASET' THEN ds.owner
        WHEN ri.type = 'CONFIG' THEN cf.owner
        WHEN ri.type = 'MODULE' THEN mo.owner
        ELSE NULL
    END AS owner
    CASE
        WHEN ri.type = 'DATASET' THEN ds.entity_id
        WHEN ri.type = 'CONFIG' THEN cf.entity_id
        WHEN ri.type = 'MODULE' THEN mo.entity_id
        ELSE NULL
    END AS entity_id
    CASE
        WHEN ri.type = 'DATASET' THEN ds.is_public
        WHEN ri.type = 'CONFIG' THEN cf.is_public
        WHEN ri.type = 'MODULE' THEN mo.is_public
        ELSE NULL
    END AS is_public
FROM
    repo_item ri
LEFT JOIN
    dataset ds ON ri.type = 'DATASET' AND ri.repo_item_id = ds.repo_item_id
LEFT JOIN
    config cf ON ri.type = 'CONFIG' AND ri.repo_item_id = cf.repo_item_id
LEFT JOIN
    module mo ON ri.type = 'MODULE' AND ri.repo_item_id = mo.repo_item_id
WHERE
    ri.repo_id = <repo_id>;


"SELECT ri.repo_item_id, ri.type, CASE WHEN ri.type = 'DATASET' THEN ds.dataset_id WHEN ri.type = 'CONFIG' THEN cf.config_id WHEN ri.type = 'MODULE' THEN mo.module_id ELSE NULL END AS ref_id, CASE WHEN ri.type = 'DATASET' THEN ds.name WHEN ri.type = 'CONFIG' THEN cf.name WHEN ri.type = 'MODULE' THEN mo.name ELSE NULL END AS file_name, CASE WHEN ri.type = 'DATASET' THEN ds.path WHEN ri.type = 'CONFIG' THEN cf.path WHEN ri.type = 'MODULE' THEN mo.path ELSE NULL END AS file_path, CASE WHEN ri.type = 'DATASET' THEN ds.description WHEN ri.type = 'CONFIG' THEN cf.description WHEN ri.type = 'MODULE' THEN mo.description ELSE NULL END AS description, CASE WHEN ri.type = 'DATASET' THEN ds.owner WHEN ri.type = 'CONFIG' THEN cf.owner WHEN ri.type = 'MODULE' THEN mo.owner ELSE NULL END AS owner, CASE WHEN ri.type = 'DATASET' THEN ds.entity_id WHEN ri.type = 'CONFIG' THEN cf.entity_id WHEN ri.type = 'MODULE' THEN mo.entity_id ELSE NULL END AS entity_id, CASE WHEN ri.type = 'DATASET' THEN ds.is_public WHEN ri.type = 'CONFIG' THEN cf.is_public WHEN ri.type = 'MODULE' THEN mo.is_public ELSE NULL END AS is_public FROM repo_item ri LEFT JOIN dataset ds ON ri.type = 'DATASET' AND ri.repo_item_id = ds.repo_item_id LEFT JOIN config cf ON ri.type = 'CONFIG' AND ri.repo_item_id = cf.repo_item_id LEFT JOIN module mo ON ri.type = 'MODULE' AND ri.repo_item_id = mo.repo_item_id WHERE ri.repo_id = <repo_id>"
