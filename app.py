from crawl import get_sitemap, convert_sitemap_to_json, get_urls_list, crawl_for_links
from process import clean_errors, clean_external_links
from pagerank import create_scoring_dict, pagerank_alg
from analyze import asc_order, desc_order, print_vals

def main():
    #Crawl sitemap ONLY RUN ONCE!
    get_sitemap(**Route to Sitemap**)
    
    #Convert xml to json ONLY RUN ONCE!
    #convert_sitemap_to_json()
    
    #Get just urls ONLY RUN ONCE!
    get_urls_list()

    #Run full crawler ONLY RUN ONCE!
    crawl_for_links()

    #clean data and make sure it's in the right format ONLY RUN ONCE
    data = clean_errors()
    clean_external_links(data)

    #Create Scoring list of dicts
    score, new_score = create_scoring_dict()

    #Run PageRank on said pages
    score = pagerank_alg(score, new_score, 10)

    #Analyze data and possibly visualize
    #sorted_asc = asc_order(score)
    #print(sorted_asc)
    #sorted_desc = desc_order(score)
    #print(sorted_desc)
    #print_vals(sorted_desc)

def dev():
    pass

if __name__ == "__main__":
    main()
    #dev()