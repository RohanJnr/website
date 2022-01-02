-- upgrade --
CREATE TABLE IF NOT EXISTS "megaprojects" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL,
    "email" VARCHAR(256) NOT NULL,
    "srn" VARCHAR(14) NOT NULL,
    "phone" INT NOT NULL,
    "department" VARCHAR(3) NOT NULL,
    "project_title" VARCHAR(128) NOT NULL,
    "project_description" TEXT NOT NULL,
    "components" TEXT NOT NULL,
    "approved" BOOL NOT NULL  DEFAULT False
);
COMMENT ON COLUMN "megaprojects"."department" IS 'CS: CS\nEC: EC\nME: ME\nECE: ECE\nBT: BT\nCE: CE';
COMMENT ON TABLE "megaprojects" IS 'MegaProjects model.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
