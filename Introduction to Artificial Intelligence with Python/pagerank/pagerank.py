import os
import random
import copy
import re
import sys
import numpy as np

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def filter_page(corpus: dict, page: str) -> set:
    '''
    Returns a correct set of links for a page
    If a page has no links, it will return all pages in the corpus
    If a page has a link to itself, it will be removed
    '''
    filterd_links = set()
    for link in corpus[page]:
        if link != page and link not in filterd_links:
            filterd_links.add(link)
    if len(filterd_links) == 0:
        for p in corpus.keys():
            filterd_links.add(p)
    return filterd_links

def filter_corpus(corpus: dict) -> dict:
    '''
    Returns a correct corpus
    Applies filter_page to all pages in the corpus
    '''
    new_corpus = dict()
    for page in corpus.keys():
        new_corpus[page] = filter_page(corpus, page)
    return new_corpus

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    filterd_corpus = filter_corpus(corpus)
    links_count  = set()
    # Adding the correct links to the set links_count
    for link in filterd_corpus[page]:
        links_count.add(link)
    probability_selecting_page = dict()
    # Calculating the probability of selecting a page and adding it to the dictionary probability_selecting_page
    for p in links_count:
        probability_selecting_page[p] = damping_factor * (1 / len(links_count)) +  ((1 - damping_factor) * (1 / len(corpus)))
    total_probability = 0
    # Normalizing the probability
    for p in probability_selecting_page.keys():
        total_probability += probability_selecting_page[p]
    for p in probability_selecting_page.keys():
        probability_selecting_page[p] /= total_probability
    return probability_selecting_page

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    new_dict = dict()
    page = np.random.choice(tuple(corpus.keys()))
    # Getting the probability of the current page, that was chosen randomly
    # Looping n times
    # Updating the current page to the next page, that was chosen using the probability of a user clicking on a link to go to that page
    for _ in range(n):
        links = transition_model(corpus, page, damping_factor)
        next_page = np.random.choice(tuple(links.keys()), p=tuple(links.values()))
        if next_page not in new_dict.keys():
            new_dict[next_page] = 1
        else:
            new_dict[next_page] += 1
        page = next_page
    # Normalizing the values
    for page in new_dict.keys():
            new_dict[page] /= n
    return new_dict

def check_values_changed(prev_ranks: dict, pages_rank: dict) -> bool:
    '''
    Returns True if the values of the pages altered more than 0.001
    '''
    for page in pages_rank.keys():
        if prev_ranks[page] > pages_rank[page] + 0.001 or prev_ranks[page] < pages_rank[page] - 0.001:
            return True
    return False

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages_rank = dict()
    # Setting the initial value of each page to 1 / number of pages
    for link in corpus.keys():
        pages_rank[link] = 1/len(corpus.keys())
    # Getting a correct corpus, using filter_corpus
    correct_links = filter_corpus(corpus)
    # Looping until the values of the pages don't change more than 0.001
    # To achieve that we save the previous values of the pages in prev_ranks and check the condition with check_values_changed
    # In each iteration we check how many times a page contains a link on another page, and we calculate the new value of the page
    # We achieve that by adding all link occurrences of a page and dividing it by the number of links on that page
    # Then we multiply it by the damping factor
    # then we add the value of (1 - damping factor) / number of pages
    # The calculated value mecioned above is then added to the previous value of the page rank
    # We do that for all pages in each iteration
    # We stop the loop when the values of the pages don't change more than 0.001, as mentioned above
    while(1):
        prev_ranks = copy.deepcopy(pages_rank)
        for page in pages_rank.keys():
            sum = 0
            for link in correct_links.keys():
                if page in correct_links[link]:
                    sum += pages_rank[link] / len(correct_links[link])
            pages_rank[page] = (1 - damping_factor) / len(corpus.keys()) + damping_factor * sum
        if not check_values_changed(prev_ranks, pages_rank):
            break
    # Normalizing the values
    total = 0
    for page in pages_rank.keys():
        total += pages_rank[page]
    for page in pages_rank.keys():
        pages_rank[page] /= total
    return pages_rank


    


if __name__ == "__main__":
    main()
