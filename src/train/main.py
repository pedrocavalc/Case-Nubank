from trainer.trainer_orchestrator import TrainerOrchestrator



def main(data_path, target, columns = None, ids = None):
    trainer = TrainerOrchestrator(data_path, target,columns= columns, ids= ids)
    trainer.run()




if __name__ == "__main__":
    columns = ["imdbId",	"title",	"type",	"genres",	"releaseYear",	"imdbAverageRating",	"imdbNumVotes",	"availableCountries", "label"]
    main(data_path="..\\..\\data\\processed\\plataform_data.csv", target="label", columns = columns,ids = ["tt0126029", "tt1396484", "tt5311514", "tt0209144", "tt0120338",])