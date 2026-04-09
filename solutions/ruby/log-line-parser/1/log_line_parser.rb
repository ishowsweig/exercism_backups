class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    start = @line.index(' ') + 1
    len = @line.length
    @line.slice(start, len).strip
  end

  def log_level
    start = @line.index('[') + 1
    finish = @line.index(']') - 1
    @line.slice(start, finish).downcase
  end

  def reformat
    self.message.capitalize + " (" + self.log_level + ")"
  end
end
