CREATE TABLE public.trinome (
	id uuid NULL,
	"date" date NULL,
	couts_carbu decimal NULL,
	couts_pneu decimal NULL,
	couts_entretien decimal NULL,
	couts_peage decimal NULL,
	salaires decimal NULL,
	cotisations decimal NULL,
	indemnites decimal NULL,
	autres_couts decimal NULL,
	assurances decimal NULL,
	taxes decimal NULL,
	couts_structure decimal NULL,
	couts_kms decimal NULL,
	couts_horaires decimal NULL,
	couts_journaliers decimal NULL,
	couts_journaliers_autres decimal NULL,
	couts_forces_fms decimal NULL,
	couts_forces_horaires decimal NULL,
	couts_forccouts_forces_journalierses_journaliers decimal NULL,
	en_vigeur bool NULL
);
CREATE INDEX trinome_id_idx ON public.trinome (id);
