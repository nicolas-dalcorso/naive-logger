#   string = f"{[string]!s:[[self.rules['FILL']]self.rules['ALIGN']][self.rules['WIDTH']]}";
import string as s

class FormattedString:
    """A class for formatting a string according to creation rules.
    """
    __slots__ = 'string', 'rules';
    DEFAULT_STRING_FORMAT = {
        'WIDTH'     : 0,
        'LENGTH'    : 0,
        'FILL'      : ' ',
        'ALIGN'     : '<'
    };

    
    def _formatString(self, string:str) -> str:
        return f"{string:{self.rules['FILL']}{self.rules['ALIGN']}.{self.rules['WIDTH']}}";
    
    def _defineRules(self, rules:dict) -> dict:
        return rules;
    
    def __init__(self, string:str, rules:dict=DEFAULT_STRING_FORMAT or str) -> None:
        self.rules  = self._defineRules(dict(rules));
        self.string = self._formatString(str(string));
        
class DTString(FormattedString):
    DEFAULT_TEMPLATE_STRING_FORMAT:dict={
        'WIDTH'     :   16,
        'LENGTH'    :   16,
        'FILL'      :   ' ',
        'ALIGN'     :   '<'
    }
    
    def _defineRules(self, rules: dict) -> dict:
        return self.DEFAULT_TEMPLATE_STRING_FORMAT;
        
    def _formatString(self, string: str) -> str:
        return super()._formatString(string);

    def __init__(self, string: str, rules: dict = DEFAULT_TEMPLATE_STRING_FORMAT or str) -> None:
        super().__init__(string, rules);      



class TextWrapper:
    __slots__ = 'filepath', 'file', 'isValid';
    
    
    #   Initialization functions;
    def _getFilepath(self, filepath:str) -> str or None:
        from os import path;
        if(path.isfile(filepath)):
            return filepath;
        else:
            return None;
    
    def _getFile(self, filepath:str):
        return open(filepath, "r+").read();
    
    def _isValid(self) -> bool:
        if(self.filepath != None):
            return True;
        return False;
            
    def __init__(self, filepath:str) -> None:
        self.filepath   = self._getFilepath(filepath);
        self.file       = self._getFile(filepath);
        self.isValid    = self._isValid();
        
        
class ConfigWrapper(TextWrapper):
    """Implements a `TextWrapper` object alongside with a `configparser`
    object from the configparser module.
    """
    DEFAULT_FILE_EXTENSION = r'.ini';
    
    def _chkFileExtension(self) -> bool:
    #   Checks if the file has the correct file extension.
        return self.filepath[-4:] == self.DEFAULT_FILE_EXTENSION;
    
    def _isValid(self) -> bool:
    #   Extends the `_isValid` checking method.
    
        if(self._chkFileExtension() != True):
            self.isValid = False;
        else:
            self.isValid = True;
    
    def __init__(self, filepath: str) -> None:
        super().__init__(filepath);
            
        import configparser
        self.parser = configparser.ConfigParser();
        self.parser.read(self.filepath);