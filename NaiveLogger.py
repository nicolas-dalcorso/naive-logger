import logging;
import logging.config
import TextWrappers as tw;

def getLoggerConfigFromFile(configFile:str) -> tw.TextWrapper:
    return tw.TextWrapper(configFile);

class NaiveLoggerFactory:
    __slots__ = 'configuration', 'logger', 'temporaryLogFilepath', 'permanentLogFilepath'
    DEFAULT_CONFIGFILE_FILEPATH:str=r'./logs/NaiveLoggerConfig.ini';
    DEFAULT_LOGS_DIRECTORY:str=r'./logs/';
    
    
    def __init__(self, mode:str='configfile', filepath:str=DEFAULT_CONFIGFILE_FILEPATH,
                 permanentLogFilepath:str=DEFAULT_LOGS_DIRECTORY + 'plog.log') -> None:
        """Initializes a `NaiveLogger` object according to the `mode` parameter.

        Args:
            mode (str, optional): 
                'configfile'    :   reads logger configuration from config '.ini' file.            
        """
        if(mode == 'configfile'):
            #   Reads configuration from file
            self.configuration  = tw.ConfigWrapper(filepath=filepath);
            
            #   Constructs logger from configuration
            logging.config.fileConfig(self.configuration.filepath);
            
        #   Initializes the logger
        self.logger                 = logging.getLogger();
        
        #   Set the filepaths
        self.temporaryLogFilepath   = self.DEFAULT_LOGS_DIRECTORY + 'temp.log';
        self.permanentLogFilepath   = permanentLogFilepath;
        
        #   Check if permanent logfile already exists
        import os
        if(os.path.exists(self.permanentLogFilepath) != True):
            open(self.permanentLogFilepath, "w");
            
    def _register(self) -> None:
        try:
            with open(self.temporaryLogFilepath, "r") as logfile:
                templogs = logfile.read();
                open(self.temporaryLogFilepath, "w");
                
        except Exception:
            return -1;
        finally:
            try:
                with open(self.permanentLogFilepath, "a+") as pfile:
                    pfile.write(templogs);
            except Exception:
                return -1;
            finally:
                return None;