-- upgrade --
ALTER TABLE "megaprojects" ALTER COLUMN "phone" TYPE VARCHAR(10) USING "phone"::VARCHAR(10);
ALTER TABLE "megaprojects" ALTER COLUMN "department" TYPE VARCHAR(2) USING "department"::VARCHAR(2);
-- downgrade --
ALTER TABLE "megaprojects" ALTER COLUMN "phone" TYPE INT USING "phone"::INT;
ALTER TABLE "megaprojects" ALTER COLUMN "department" TYPE VARCHAR(3) USING "department"::VARCHAR(3);
